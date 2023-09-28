# model/product.py

from flask_mongoengine import MongoEngine
from models.custom_error import CustomError

db = MongoEngine()

class Product:
    def __init__(self,id,name,description,price):
        self.id=id
        self._validate_name(name)
        self.name=name
        self._validate_description(description)
        self.description=description
        self.price=price

    def convert_to_dictionary(self):
        return {'id': self.id,'name': self.name,'decription': self.description,'price': self.price}

    def _validate_name(self,name):
        if not name or not isinstance(name,str):
            raise CustomError("Name is not valid")

    def _validate_description(self,description):
        if not description or not isinstance(description,str) or len(description)<10:
            raise CustomError('Description is not valid')

