!#/usr/bin python3
""" One base model to rule them all """
import uuid
import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[BaseModel] ({}) <{}>".format(self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        self_dict = {
            '__class__': 'BaseModel',
            'id': self.id,
            'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'upated_at': self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        }
