"""Module with the Blueprint of the To Do's API.
"""
from flask import Blueprint
todo_views = Blueprint('todo_views', __name__, url_prefix='/api/todos')
from views.todo_view import *
