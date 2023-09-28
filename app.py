from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_mongoengine import MongoEngine
import os
import uuid

from helpers import config
from models.product import Product
from models.list_product import ListProduct
from models.custom_error import CustomError
from routers import product_router

app=Flask(__name__)

list_product=ListProduct()

@app.route('/api/products', methods=['POST'])
def create_product_handler():
    return product_router.create_product(list_product,request)

@app.route('/api/products',methods=['GET'])
def retrieve_all_products_handler():
    return product_router.retrieve_all_products(list_product)

@app.route('/api/products/<product_id>',methods=['GET'])
def retrieve_product_by_id_handler(product_id):
    return product_router.retrieve_product_by_id(list_product,product_id)

@app.route('/api/products/<product_id>/name',methods=['PUT'])
def edit_name_product_by_id_handler(product_id):
    return product_router.edit_name_product_by_id_handler(product_id,list_product,request)

@app.route('/api/products/<product_id>/description',methods=['PUT'])
def edit_description_product_by_id_handler(product_id):
    return product_router.edit_description_product_by_id_handler(product_id,list_product,request)

@app.route('/api/products/<product_id>/price',methods=['PUT'])
def edit_price_product_by_id_handler(product_id):
    return product_router.edit_price_product_by_id_handler(product_id,list_product,request)

@app.route('/api/products/<product_id>',methods=['DELETE'])
def delete_price_product_by_id_handler(product_id):
    return product_router.delete_price_product_by_id_handler(product_id,list_product)

if __name__ == '__main__':
    app.run(debug=True, port=config.PORT)