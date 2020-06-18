"""Module with the route handlers for the To Do's API.
"""
from views import todo_views
from flask import (abort, jsonify, request)
from app import todos
from todo_model import Todo


def create_todo(text):
    """Saves a To Do in the list.

    Args:
        text (str): the text if the To Do.

    Returns:
        [Todo]: an array with all the To Do's.
    """
    new_todo = Todo(text)
    todos[new_todo.id] = new_todo
    return todos


def update_todo(todo_id, text=None, completed=None):
    """Updates the state of a To Do in the list according to its id.

    Args:
        todo_id (str):              the UUID of the To Do.
        text (str, optional):       the new text of the To Do.
                                    Defaults to None to avoid its update.
        completed (bool, optional): the status of the To Do.
                                    Defaults to None to avoid its update.

    Returns:
        [Todo]: an array with all the To Do's.
    """
    if todo_id in todos:
        todo = todos[todo_id]
        todo.update_todo(text, completed)
    return todos


def delete_todo(todo_id):
    """Deletes a To Do From the list if it exists.

    Args:
        todo_id (str):  the UUID of the To Do.

    Returns:
        [Todo]: an array with all the To Do's.
    """
    if todo_id in todos:
        del todos[todo_id]
    return todos


def get_todos(todo_id=None):
    """Retrive every To Do or a specific To Do with its UUID.

    Args:
        todo_id (str, optional):    the UUID of the To Do. Defaults to None if
                                    there isn't required a specific To Do.

    Returns:
        [Todo]: an array with all the To Do's in JSON representation.
    """
    if not todo_id:
        return jsonify([todo.to_json() for todo in todos.values()])
    else:
        if todo_id in todos:
            requested_todo = todos[todo_id].to_json()
            return jsonify(requested_todo)


@todo_views.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def todos_handler():
    """Handle the HTTP requests for all the methods supported and
    updates the To Do's list only if it's a valid request.

    Returns:
        [Todo]: an array with all the To Do's in JSON representation.
    """
    method = request.method
    data = request.get_json()

    if method in ('POST', 'PUT'):
        text = data.get('text')
        if not text:
            abort('404', 'Missing text')

    if method in ('PUT', 'DELETE'):
        todo_id = data.get('id')
        if not todo_id:
            abort('404', 'Missing text')

    if method == 'GET':
        return get_todos()

    if method == 'POST':
        new_todo = create_todo(text)
        return (jsonify({'new_todo': new_todo}), 201)

    if method == 'PUT':
        updated_todo = update_todo(todo_id, text)
        return (jsonify({'updated_todo': updated_todo}), 200)

    if method == 'DELETE':
        delete_todo(todo_id)
        return ("Todo deleted", 200)


@todo_views.route('/<todo_id>')
def get_todo_handler(todo_id):
    """Get a specific To Do.

    Args:
        todo_id (str): the UUID of the To Do.

    Returns:
        [Todo]: an array with all the To Do's.
    """
    if todo_id in todos:
        return get_todos(todo_id)
