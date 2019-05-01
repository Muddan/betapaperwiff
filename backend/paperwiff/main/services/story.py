from flask import g
import datetime
from  paperwiff.main import get_db
from pymongo import DESCENDING as decending
from ..services.user import UserClass

userService = UserClass()

class StoryClass:
    def __init__(self):
        db = get_db()
        self.storyCollection = db['stories']
        self.tagsCollection = db['tags']

    def publishStory(self, userId, tags, storyTitle, content):
        userData = userService.getUsernameByUserId(userId)
        newStory = {
            "storyId": storyTitle.lower().replace(" ", "-"),
            "userId": userId,
            "userName": userData["userName"],
            "storyTitle": storyTitle,
            "content": content,
            "tags": tags,
            "likes": 0,
            "datePublished": (str(datetime.datetime.now())),
            "comment":[]
        }
        try:
            self.storyCollection.insert_one(newStory)
            return {
                "msg": 'Successfully saved the story',
                "status": 200
            }
        except:
            return {
                "msg": 'Error saving story',
                "status": 400
            }


    def addComment(self,Input_json):
        try:
            print(Input_json)
            self.storyCollection.find_one_and_update({"storyId": str(Input_json["storyId"])}, {"$push": {"comments": {
                "comment": Input_json["comment"],
                "date": Input_json["date"],
                "userName":Input_json["userName"]
            }}})
        except:
            if not Input_json.get("storyId") :
                return {
                    "msg": 'Error Adding storyID not found',
                    "status": 400
                }

            if not Input_json.get("userId"):
                return {
                    "msg": 'Error Adding Comment please login to add comment',
                    "status": 400
                }

            if not Input_json.get("comments") :
                return {
                    "msg": 'Error Adding Comment, comment can not be empty',
                    "status": 400
                }

            if Input_json.get("date") == None:
                return {
                    "msg": 'Error Adding Comment, date has not been passed',
                    "status": 400
                }

            else:
                return {
                    "msg": 'Error Adding Comment, Something went wrongs',
                    "status": 400
                }


    def getAllAvailableTags(self):
        tags = self.tagsCollection.find({}, {"_id": False})
        return list(tags)

    def getAllStories(self):
        stories = self.storyCollection.find(projection={
            "_id": False
        }).limit(20).sort("datePublished", decending)
        for story in stories:

            image = self.userCollection.find_one({"userId": story["userId"]}, projection={
                "_id": False, 'userImage': True})
            story.update(image)
            print(story)
        return list(stories)

    def getStoryDetailsByStoryId(self, storyId):
        storyDetails = self.storyCollection.find(
            {"storyId": storyId},
            projection={"_id": False}
        )
        return list(storyDetails)