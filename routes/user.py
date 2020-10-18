import os
from flask import Blueprint, jsonify, request, current_app, render_template
from flask_pymongo import pymongo, ObjectId

#Database connection information
CONNECTION_STRING = f"mongodb+srv://sacm:{os.getenv('MONGO_DB_PASSWORD')}@cluster0.7etez.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
#Database Name
db = client.get_database('app_database')
table = db.user


route_users = Blueprint('route_users', __name__)

@route_users.route('/users', methods=['POST'])
def createUser():
    id = table.insert({
        'username': request.json['username'],
        'password': request.json['password']
    })
    return jsonify(str(ObjectId(id))), 200

@route_users.route('/users', methods=['GET'])
def getUsers():
    users=[]
    for doc in table.find():
        users.append({
            '_id': str(ObjectId(doc['_id']))
        })
    return jsonify(users), 200

@route_users.route('/user/<id>', methods=['DELETE'])
def deleteUser(id):
    table.delete_one({'_id': ObjectId(id)})
    return jsonify({'success': 'usuario eliminado'})
