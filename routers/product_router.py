from flask import Flask, jsonify, request
import uuid

from helpers import config
from models.product import Product
from models.list_product import ListProduct
from models.custom_error import CustomError


def create_product(list_product,request):
    try:
        data = request.get_json()
        try:
            product=Product(str(uuid.uuid4()),data.get('name'),data.get('description'),data.get('price'))
            list_product.list.append(product)
            return jsonify({"message": "the object has been successfully created","created_object": product.convert_to_dictionary()}),200
        except CustomError as e:
            return jsonify({'error': str(e)}),404        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

def retrieve_all_products(list_product):
    try:
        result={}
        for item in list_product.list:
            result[item.id]={"name":item.name,"description":item.description,"price":item.price}
        return jsonify(result),200    
    except Exception as e:
        return jsonify({'error': str(e)}),500
    

def retrieve_product_by_id(list_product,product_id):
    try:
        if len(product_id)<10:
            return jsonify({'message': 'the id is not valid'}),400
        result=None
        for item in list_product.list:
            if item.id==product_id:
                result=item
                break
        if not result:
            return jsonify({'message': 'there is no product matching this id'}),404
        return jsonify({'result': item.convert_to_dictionary()}),200
    except Exception as e:
        return jsonify({'error': str(e)}),500
    
def edit_name_product_by_id_handler(product_id,list_product,request):
    try:
        if len(product_id)<10:
            return jsonify({'message': 'the id is not valid'}),400
        data=request.get_json()
        if not data.get('name'):
            return jsonify({'message': 'the name filed is not valid'}),400
        result=None
        for item in list_product.list:
            if item.id==product_id:
                result=item
                break
        if not result:
            return jsonify({'message': 'there is no product matching this id'}),404
        result.description=data.get('name')
        return jsonify({'message': 'the product has been updated','result': item.convert_to_dictionary()}),200
    except Exception as e:
        return jsonify({'error': str(e)}),500
    

def edit_price_product_by_id_handler(product_id,list_product,request):
    try:
        if len(product_id)<10:
            return jsonify({'message': 'the id is not valid'}),400
        data=request.get_json()
        if not data.get('price'):
            return jsonify({'message': 'the name filed is not valid'}),400
        result=None
        for item in list_product.list:
            if item.id==product_id:
                result=item
                break
        if not result:
            return jsonify({'message': 'there is no product matching this id'}),404
        result.price=int(data.get('price'))
        return jsonify({'message': 'the product has been updated','result': item.convert_to_dictionary()}),200
    except Exception as e:
        return jsonify({'error': str(e)}),500
    

def delete_price_product_by_id_handler(product_id,list_product):
    try:
        if len(product_id)<10:
            return jsonify({'message': 'the id is not valid'}),400
        count=0
        result=None
        for item in list_product.list:
            if item.id==product_id:
                result=item
                list_product.list.pop(count)
                break
            count+=1
        if not result:
            return jsonify({'message': 'there is no product matching this id'}),404
        return jsonify({'message': 'the product has been deleted','result': result.convert_to_dictionary()}),200
    except Exception as e:
        return jsonify({'error': str(e)}),500