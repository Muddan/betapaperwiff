from flask import Blueprint, request, jsonify, json
from ..services.user import UserClass

from flask_jwt_extended import jwt_required, get_jwt_identity

User = Blueprint('user', __name__)

userServices = UserClass()


@User.route('/details', methods=['POST'])
def userDetails():
    try:
        data_json = json.loads(request.data)
        userName = data_json['userName']
        response = userServices.getUserDetailsByuserName(userName)
        return jsonify(response), 200
    except:
        return jsonify({
            "message": 'userName does not exist, please try again',
            "status": 400
        }), 400


@User.route('/followtag', methods=['POST'])
@jwt_required
def followTag():
    try:
        data_json = json.loads(request.data)

        if not data_json.get('userId'):
            return jsonify({
                "message": 'userId missing, please try again',
                "status": 400
            }), 400

        if not data_json.get('tag'):
            return jsonify({
                "message": 'tag missing, please try again',
                "status": 400
            }), 400

        if not userServices.userExistsInCollection(data_json['userId']):
            return jsonify({
                "message": 'userId does not exist, please try again',
                "status": 400
            }), 400

        userId = data_json['userId']
        tag = data_json['tag']

        response = userServices.addFollowingTag(userId, tag)

        return jsonify(response), response['status']

    except ValueError:
        print(ValueError)
        return jsonify({
            "Message": "Something went wrong while saving tags"
        }), 400
