""" Module with the data model of a To Do.
"""
from datetime import datetime
from uuid import uuid4


class Todo:
    """Represents a basic To Do with status and dates.
    """

    def __init__(self, description: str):
        """Initialize a To Do.

        Args:
            description (str): the data contained in the To Do.
        """
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.id = str(uuid4())
        self.completed = False

    def update_todo(self, description, completed):
        """Update a To Do with new valid fields.

        Args:
            description (str): the data contained in the To Do.
            completed (bool): the status of the To Do.
        """
        if description:
            self.description = description
        self.completed = completed
        self.updated_at = datetime.now()

    def to_json(self):
        """Creates a valid JSON representation of a To Do.

        Returns:
            (str): a valid JSON representation of a To Do with all its data.
        """
        representation = {
            field: (
                value.strftime("%m/%d/%Y, %H:%M:%S")
                if isinstance(value, datetime)
                else value)
            for field, value in self.__dict__.items()
        }
        return(representation)
