from flask import Blueprint, request, jsonify, json, make_response
from ..services.story import StoryClass
from ..services.user import UserClass

from flask_jwt_extended import jwt_required, get_jwt_identity
from translate import Translator

# Response helper
from ..helpers.response import response
from ..helpers.UserServiceHelper import UserServiceHelper

Story = Blueprint('story', __name__)

storyService = StoryClass()
userService = UserClass()


@Story.route('/alltags', methods=['GET'])
def allTags():
    try:
        result = storyService.getAllAvailableTags()
        return response(result), result['status']
    except Exception as e:
        return response("Something went wrong while retrieving tags: " + str(e)), 400


# @Story.route('/allstories/popular', methods=['GET'])
# def allPopularStories():
#     if not request.args.get('pageNo'):
#         page = 1
#     else:
#         page = int(request.args.get('pageNo'))
#     try:
#         result = storyService.getAllPopularStories(page)
#         return make_response(response(result), result['status'])
#     except Exception as e:
#         return make_response(response('Something went wrong while getting stories ' + str(e)), 400)

@Story.route('/tag/stories', methods=['GET'])
def taggedStories():
    if not request.args.get('pageNo'):
        pageNo = 1
    else:
        pageNo = int(request.args.get('pageNo'))
    if not request.args.get('tag'):
        return 'try again'

    tagName = request.args.get('tag')

    result = storyService.getTagStories(pageNo=pageNo, tagName=tagName)
    return make_response(response(result), result.get('status'))


@Story.route('/allstories', methods=['GET'])
def allStories():
    if not request.args.get('pageNo'):
        pageNo = 1
    else:
        pageNo = int(request.args.get('pageNo'))

    result = storyService.getAllStories(pageNo=pageNo)
    return make_response(response(result), result.get('status'))


@Story.route('/authorStories', methods=['GET'])
def authorstories():
    if not request.args.get('pageNo'):
        pageNo = 1
    else:
        pageNo = int(request.args.get('pageNo'))
    if not request.args.get('userName'):
        return 'Invalid username', 400

    userName = request.args.get('userName')

    result = storyService.getAuthorStories(pageNo=pageNo, userName=userName)
    return make_response(response(result), result.get('status'))


@Story.route('/userStories', methods=['GET'])
def userStories():
    if not request.args.get('pageNo'):
        pageNo = 1
    else:
        pageNo = int(request.args.get('pageNo'))
    if not request.args.get('userId'):
        return 'Invalid username', 400

    userId = request.args.get('userId')

    result = storyService.getUserStories(pageNo=pageNo, userId=userId)
    return make_response(response(result), result.get('status'))
    # try:

    #     if  request.args.get('userId')==None and request.args.get('userName')==None:
    #         result = storyService.getAllStories(pageNo=pageNo)
    #         return make_response(response(result), result.get('status'))

    #     elif request.args.get('userId'):
    #         userId = request.args.get('userId')
    #         if not userService.userExistsInCollection(userId):
    #             return response('userId does not exist, please try again'), 400
    #         result = storyService.getCustomizedStories(pageNo=pageNo, userId=userId)
    #         return make_response(response(result), result['status'])

    #     else:
    #         userName = request.args.get('userName')
    #         if not userService.userNameExistsInCollection(userName):
    #             return response('userName does not exist, please try again'), 400
    #         result = storyService.getUserStories(pageNo=pageNo, userName=userName)
    #         return make_response(response(result), result['status'])

    # except Exception as e:
    #     return make_response(response('Something went wrong while getting stories ' + str(e)), 400)


# @Story.route('/comment', methods=['POST'])
# def CommentAdd():
#     try:
#         data_json = request.get_json(request.data)
#         result = storyService.addComment(data_json)
#         return response(result), result['status']
#     except Exception as e:
#         return response("Something went wrong while retrieving tags: " + str(e)), 400


@Story.route('/publish', methods=['POST'])
@jwt_required
def publishStory():
    try:
        data_json = request.get_json(request.data)

        if not request.get_json('userId'):
            return response('userId missing, please try again'), 400

        if not request.get_json('tags'):
            return response('tags are missing, please try again'), 400

        if not request.get_json('storyTitle'):
            return response('Story title should be provided'), 400

        if not UserServiceHelper().userIdExists(data_json['userId']):
            return response('userId does not exist, please try again'), 400

        if not data_json.get('datePublished'):
            return response("Datepublished is missing, please try again"), 400

        if not data_json.get('language'):
            return response("language is missing, please try again"), 400

        userId = data_json['userId']
        tags = list(data_json['tags'])
        storyTitle = data_json['storyTitle']
        content = data_json['content']
        language = data_json['language']
        datePublished = data_json["datePublished"]
        headerImage = data_json["headerImage"]
        summary = data_json["summary"]
        result = storyService.publishStory(userId=userId, tags=tags, summary=summary,
                                           storyTitle=storyTitle, content=content, language=language, datePublished=datePublished, headerImage=headerImage)
        return response(result), result['status']

    except Exception as e:
        return response(str(e)), 400


@Story.route('/details', methods=['POST'])
def storyDetails():
    try:
        data_json = request.get_json(request.data)

        if not request.get_json('storyId'):
            return response('storyId missing, please try again'), 400

        storyId = data_json.get('storyId')
        storyDetails = storyService.getStoryDetailsByStoryId(storyId)
        return response(storyDetails), storyDetails['status']
    except Exception as e:
        return response('Exception ' + str(e)), 400


@Story.route('/popular', methods=['GET'])
def popularStories():
    result = storyService.getPopularStories()
    return make_response(response(result), result.get('status'))


@Story.route('/delete', methods=['POST'])
def deleteStories():
    try:
        data_json = request.get_json(request.data)
        if not data_json.get('storyId'):
            return response('storyIds are missing, please try again'), 400
        storyId = data_json.get('storyId')
        result = storyService.deleteByStoryId(storyId)
        return response(result), result['status']
    except Exception as e:
        return response('Exception ' + str(e)), 400
