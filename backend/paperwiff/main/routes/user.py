from flask import Blueprint, request, jsonify, json, make_response

from ..helpers import addToArray
from ..services.user import UserClass
from flask_jwt_extended import jwt_required, get_jwt_identity

# Response Helper
from ..helpers.response import response

User = Blueprint('user', __name__)

userServices = UserClass()


@User.route('/details', methods=['POST'])
def userDetails():
    try:
        data_json = json.loads(request.data)
        userName = data_json['userName']
        result = userServices.getUserDetailsByuserName(userName)
        return make_response(response(result), 200)
    except Exception as e:
            return make_response(response(str(e)), 400)


@User.route('/followtag', methods=['POST'])
@jwt_required
def followTag():
    try:
        data_json = json.loads(request.data)

        if not data_json.get('userId'):
            return make_response(response('userId missing, please try again'), 400)
        if not data_json.get('tag'):
            return make_response(response('tag missing, please try again'), 400)

        if not userServices.userExistsInCollection(data_json['userId']):
            return make_response(response('userId does not exist, please try again'), 400)

        userId = data_json.get('userId')
        tag = data_json.get('tag')

        result = userServices.FollowTag(userId, tag)
        return make_response(response(result), result['status'])

    except Exception as e:
        return make_response(response(str(e)), 400)

@User.route('/updateUser', methods=['POST'])
def updateUserDetails():
    try:
        data_json = request.get_json(request.data)
        userId = data_json.get('userId')
        result = userServices.getUserDetailsByUserId(userId)
        if result is not None:
            return make_response(response(userServices.updateUserDetails(data_json)),200)
        return make_response(response("userId not present"), result.get('status'))
    except Exception as e:
            return make_response(response("Error occured :"+str(e)), 400)


@User.route('/saveForLater', methods=['POST'])
def readLater():
    Input = request.get_json(request.data)
    try:
        userId = Input["userId"]
        storyId = Input.get("storyId")
        result = addToArray.addToArrayUser(MongoDbFieldName="saveForLater", Value=storyId, userId=userId)
        return make_response(response(result), 200)

    except Exception as e:
        return response({
            "msg": str(e),
            "status": 400
        })