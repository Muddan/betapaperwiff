from flask import Blueprint, request, jsonify, json, make_response
from ..services.story import StoryClass
from ..services.user import UserClass

from flask_jwt_extended import jwt_required, get_jwt_identity
from translate import Translator

# Response helper
from  ..helpers.response import response

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

@Story.route('/allstories', methods=['GET'])
def allStories():
    if not request.args['pageNo']:
        page = 1
    else:
        page = int(request.args['pageNo'])
    try:
        result = storyService.getAllStories(page)
        return make_response(response(result), result['status'])
    except Exception as e:
        return make_response(response('Something went wrong while getting stories ' + str(e)), 400)


@Story.route('/allstories/popular', methods=['GET'])
def allPopularStories():
    if not request.args['pageNo']:
        page = 1
    else:
        page = int(request.args['pageNo'])
    try:
        result = storyService.getAllPopularStories(page)
        return make_response(response(result), result['status'])
    except Exception as e:
        return make_response(response('Something went wrong while getting stories ' + str(e)), 400)



@Story.route('/comment', methods=['POST'])
def CommentAdd():
    try:
        data_json = request.get_json(request.data)
        result = storyService.addComment(data_json)
        return response(result), result['status']
    except Exception as e:
            return response("Something went wrong while retrieving tags: " + str(e)), 400



@Story.route('/publish', methods=['POST'])
#@jwt_required
def publishStory():

    try:
        data_json = request.get_json(request.data)

        if not request.get_json('userId'):
            return response('userId missing, please try again'), 400

        if not request.get_json('tags'):
            return response('tags are missing, please try again'), 400


        if not request.get_json('storyTitle'):
            return response('Story title should be provided'), 400

        if not userService.userExistsInCollection(data_json['userId']):
            return response('userId does not exist, please try again'), 400

        if not data_json.get('datePublished'):
            return response("Faggot where's the date you told you'll take care of it"), 400

        if not data_json.get('language'):
            return response("language must be specified"), 400

        userId = data_json['userId']
        tags = data_json['tags']
        storyTitle = data_json['storyTitle']
        content = data_json['content']
        language = data_json['language']
        datePublished = data_json["datePublished"]
        result = storyService.publishStory(userId=userId, tags=tags,
                                             storyTitle=storyTitle, content=content, language=language, datePublished=datePublished)
        return make_response(response(result), result['status'])

    except Exception as e:
            return response(str(e)), 400


@Story.route('/storydetails', methods=['POST'])
def storyDetails():
    try:
        data_json = request.get_json(request.data)

        if not request.get_json('storyId'):
            return response('storyId missing, please try again'), 400

        storyId = data_json.get('storyId')
        storyDetails = storyService.getStoryDetailsByStoryId(storyId)
        return response(storyDetails), storyDetails['status']
    except Exception as e:
        return response(str(e)), 400

# @Story.route("/translate", methods=["POST"])
# def translate():
#     request_data = request.get_json()
#     dataToTranslate = {
#         "query": request_data["query"],
#         "language": request_data["language"]
#     }
#     translatedData = (translateData(dataToTranslate))
#     return jsonify({
#         "message": translatedData,
#         "status": 200
#     }), 200


# def translateData(Input_json):
#     translator = Translator(to_lang=Input_json["language"])
#     translation = translator.translate(Input_json["query"])
#     return translation
