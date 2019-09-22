#!/bin/bash/python3 flask

from flask import Flask, jsonify, request
from flask import current_app
from cloud_service import CloudService as CS
import os

app = Flask(__name__)
#CORS(app)
# Create class objects
cloud_service_obj = CS()


@app.route('/users')
def get_list_passwd_users():
    return jsonify(cloud_service_obj.get_passwd_users())

@app.route('/users/query')
def get_list_passwd_users_from_parameters():
    query_params = {'name':request.args.get('name', None)
            , 'uid':request.args.get('uid', None)
            , 'gid':request.args.get('gid',None)
            , 'comment':request.args.get('comment',None)
            , 'home':request.args.get('home',None)
            , 'shell':request.args.get('shell',None)
            }

    cloud_service_obj.validate_query_parameters(query_params)

    if len(cloud_service_obj.valid_params) == 0:
        return jsonify('[]')
    else:
        cloud_service_obj.get_passwd_users_using_query_parameters(cloud_service_obj.valid_params)
        return jsonify(cloud_service_obj.passwd_users_match_params)

@app.route('/groups/query')
def get_list_group_users_from_parameters():
    query_params = {'name':request.args.get('name', None)
            , 'gid':request.args.get('gid',None)
            , 'members':request.args.getlist('member',None)
            }

    cloud_service_obj.validate_query_parameters(query_params)

    if len(cloud_service_obj.valid_params) == 0:
        return jsonify('[]')
    else:
        cloud_service_obj.get_group_users_using_query_parameters(cloud_service_obj.valid_params)
        return jsonify(cloud_service_obj.group_users_match_params)

@app.route('/users/<uid>')
def get_single_user(uid):
    #print(uid)
    return jsonify(cloud_service_obj.get_single_user_from_uid(uid))

@app.route('/users/<uid>/groups')
def get_all_groups_for_user(uid):
    #print(uid)
    return jsonify(cloud_service_obj.get_all_groups_for_user_from_uid(uid))

@app.route('/groups')
def get_list_group_users():
    return jsonify(cloud_service_obj.get_group_users())

@app.route('/groups/<gid>')
def get_single_group(gid):
    return jsonify(cloud_service_obj.get_single_group_from_gid(gid))


if __name__ == '__main__':
    app.run(threaded=True)
