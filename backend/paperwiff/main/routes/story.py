from flask import Blueprint, request, jsonify, json
from ..services.story import StoryClass
from ..services.user import UserClass

from flask_jwt_extended import jwt_required, get_jwt_identity
from translate import Translator


Story = Blueprint('story', __name__)

storyService = StoryClass()
userService = UserClass()


@Story.route('/alltags', methods=['GET'])
def allTags():
    try:
        result = storyService.getAllAvailableTags()
        return jsonify(result), 200
    except:
        return jsonify({
            "message": 'Somethingwent wrong while getting tags',
            "status": 400
        }), 400


@Story.route('/allstories', methods=['GET'])
def allStories():
    try:
        result = storyService.getAllStories()
        return jsonify(result), 200
    except:
        return jsonify({
            "message": 'Somethingwent wrong while getting tags',
            "status": 400
        }), 400


@Story.route('/publish', methods=['POST'])
def publishStory():
    data_json = json.loads(request.data)

    if not data_json.get('userId'):
        return jsonify({
            "message": 'userId missing, please try again',
            "status": 400
        }), 400

    if not data_json.get('tags'):
        return jsonify({
            "message": 'tags are missing, please try again',
            "status": 400
        }), 400
    if not data_json.get('storyTitle'):
        return jsonify({
            "message": 'Story title is missing, please try again',
            "status": 400
        }), 400

    if not userService.userExistsInCollection(data_json['userId']):
        return jsonify({
            "message": 'userId does not exist, please try again',
            "status": 400
        }), 400

    userId = data_json['userId']
    tags = data_json['tags']
    storyTitle = data_json['storyTitle']
    content = data_json['content']
    response = storyService.publishStory(userId=userId, tags=tags,
                                         storyTitle=storyTitle, content=content)

    return jsonify(response), response['status']


@Story.route('/storydetails', methods=['POST'])
def storyDetails():
    try:
        data_json = json.loads(request.data)

        if not data_json.get('storyId'):
            return jsonify({
                "message": 'storyId missing, please try again',
                "status": 400
            }), 400
        storyId = data_json.get('storyId')
        storyDetails = storyService.getStoryDetailsByStoryId(storyId)
        return jsonify({
            "details": storyDetails,
        }), 200
    except:
        return jsonify({
            "message": 'fucked up',
            "status": 400
        }), 400


@Story.route("/translate", methods=["POST"])
def translate():
    request_data = request.get_json()
    dataToTranslate = {
        "query": request_data["query"],
        "language": request_data["language"]
    }
    translatedData = (translateData(dataToTranslate))
    return jsonify({
        "message": translatedData,
        "status": 200
    }), 200


def translateData(Input_json):
    translator = Translator(to_lang=Input_json["language"])
    translation = translator.translate(Input_json["query"])
    return translation
