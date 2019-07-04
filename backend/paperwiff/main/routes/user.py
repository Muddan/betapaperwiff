from flask import Blueprint, request, jsonify, json, make_response
from ..services.user import UserClass

from flask_jwt_extended import jwt_required, get_jwt_identity

# Response Helper
from ..helpers.response import response
from ..helpers.UserServiceHelper import UserServiceHelper
User = Blueprint('user', __name__)

userServices = UserClass()


@User.route('/details', methods=['POST'])
@jwt_required
def userDetails():
    try:
        data_json = json.loads(request.data)
        userId = data_json['userId']
        result = json.loads(
            UserServiceHelper().getUserDetailsByUserId(userId).first().to_json())
        return make_response(response(result), 200)
    except Exception as e:
        return make_response(response(str(e)), 400)


@User.route('/updateUser', methods=['POST'])
@jwt_required
def updateUserDetails():
    try:
        data_json = json.loads(request.data)
        userId = data_json.get('userId')
        result = userServices.getUserDetailsByUserId(userId)
        if result:
            return make_response(response(userServices.updateUserDetails(data_json)), 200)
        return make_response(response("userId not present"), result.get('status'))
    except Exception as e:

        return make_response(response("Error occured :"+str(e)), 400)


@User.route('/authorDetails', methods=['POST'])
def authorDetails():
    try:
        data_json = json.loads(request.data)
        userName = data_json['userName']
        if UserServiceHelper().userNameExists(userName):
            result = userServices.getAuthorDetails(userName)
            return make_response(response(result), result['status'])
        else:
            return make_response(response('Invalid userId'), 400)

    except Exception as e:
        return make_response(response(str(e)), 400)


@User.route('/follow/tag', methods=['POST'])
@jwt_required
def followTag():
    try:
        data_json = json.loads(request.data)

        if not data_json.get('userId'):
            return make_response(response('userId missing, please try again'), 400)
        if not data_json.get('tags'):
            return make_response(response('tags are missing, please try again'), 400)

        userId = data_json.get('userId')
        tags = data_json.get('tags')

        result = userServices.followTags(userId, tags)
        return make_response(response(result), result['status'])

    except Exception as e:
        return make_response(response(str(e)), 400)


@User.route('/follow/author', methods=['POST'])
@jwt_required
def followAuthor():
    try:
        data_json = json.loads(request.data)

        if not data_json.get('userId'):
            return make_response(response('userId missing, please try again'), 400)
        if not data_json.get('authorId'):
            return make_response(response('authorId  missing, please try again'), 400)

        userId = data_json.get('userId')
        authorId = data_json.get('authorId')
        result = userServices.followAuthor(userId, authorId)
        return make_response(response(result), result['status'])

    except Exception as e:
        return make_response(response(str(e)), 400)


@User.route('/story/like', methods=['POST'])
@jwt_required
def storyLike():
    try:
        data_json = request.get_json(request.data)
        if not data_json.get('storyId'):
            return make_response(response('storyId missing, please try again'), 400)
        if not data_json.get('userId'):
            return make_response(response('userId missing, please try again'), 400)

        storyId = data_json.get('storyId')
        userId = data_json.get('userId')
        result = userServices.storyLikes(storyId=storyId, userId=userId)
        return make_response(response(result), result['status'])
    except Exception as e:
        return response(str(e)), 400


@User.route('/story/save', methods=['POST'])
@jwt_required
def storySave():
    try:
        data_json = request.get_json(request.data)
        if not data_json.get('storyId'):
            return make_response(response('storyId missing, please try again'), 400)
        if not data_json.get('userId'):
            return make_response(response('userId missing, please try again'), 400)

        storyId = data_json.get('storyId')
        userId = data_json.get('userId')
        result = userServices.storySave(storyId=storyId, userId=userId)
        return make_response(response(result), result['status'])
    except Exception as e:
        return response(str(e)), 400


@User.route('/savedstories', methods=['POST'])
def savedStories():
    try:
        data_json = request.get_json(request.data)
        if not data_json.get('userId'):
            return make_response(response('userId missing, please try again'), 400)
        userId = data_json.get('userId')
        result = userServices.getUserSavedStories(userId=userId)
        return make_response(response(result), result['status'])
    except Exception as e:
        return response(str(e)), 400


@User.route('/feed', methods=['GET'])
def userFeed():
    try:
        if not request.args.get('userId'):
            return make_response(response('userId missing, please try again'), 400)
        userId = request.args.get('userId')

        # Check if userId is valid
        if not UserServiceHelper().userIdExists(userId):
            return make_response(response('Invalid userId, please try again'), 400)

        if not request.args.get('pageNo'):
            pageNo = 1
        else:
            pageNo = int(request.args.get('pageNo'))

        result = userServices.getCustomizedStories(userId=userId, pageNo=pageNo)
        return make_response(response(result), result['status'])
    except Exception as e:
        return response(str(e)), 400
