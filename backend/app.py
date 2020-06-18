"""Module with the configuration of the To Do's API.
"""
from flask import (Flask, jsonify, make_response)
from flask_cors import (CORS, cross_origin)
from todo_model import Todo
from views import todo_views

# Create api instance
app = Flask(__name__)
# Set view for todos
app.register_blueprint(todo_views)
app.url_map.strict_slashes = False
# Set cors to enable extern requests
cors = CORS(app, resources={r'/api/todos/*': {'origins': '*'}})

@app.route("/")
def hello():
    """Alerts use of incorrect entrypoint.

    Returns:
        str: a JSON representation that notifies the error.
    """
    return jsonify({"Error": "this isn't a valid entrypoint"})


@app.errorhandler(404)
def handle_404(exception):
    """A simple error handler for a 404 Not Found error.

    Args:
        exception (werkzeug.exceptions.HTTPException ): a HTTP Error
                                                        produced by a bad
                                                        request.
    Returns:
        str: a JSON representation that notifies the error.
    """
    print(exception)
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


if __name__ == "__main__":
    app.run(port=50090)
