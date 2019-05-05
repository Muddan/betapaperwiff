from flask import g
import datetime
import re
from paperwiff.main import get_db
from pymongo import DESCENDING as decending

from ..services.user import UserClass
userService = UserClass()


class StoryClass:
    def __init__(self):
        db = get_db()
        self.storyCollection = db['stories']
        self.tagsCollection = db['tags']
        self.userCollection = db['users']


    def publishStory(self, userId, tags, storyTitle, content, language, datePublished):
        userData = userService.getUsernameByUserId(userId)
        storyId = re.sub('[^A-Za-z0-9-"-"]+', '',
                         storyTitle.lower().replace(" ", "-"))
        newStory = {
            "storyId": storyId,
            "userId": userId,
            "userName": userData["userName"],
            "storyTitle": storyTitle,
            "content": content,
            "tags": tags,
            "likes": 0,
            "datePublished": datePublished,
            "comments": [],
            "language": language,
            "saveLater": []
        }
        try:
            self.storyCollection.insert_one(newStory)
            return {
                "msg": "Successfully saved the story",
                "status": 200
            }

        except Exception as e:
            return {
                "msg": "Error occurred saving story" + str(e),
                "status": 200
            }

    def addComment(self, Input_json):
        try:
            x = self.storyCollection.find_one_and_update(
                {"storyId": str(Input_json["storyId"])},
                {"$push": {"comments": {
                "comment": Input_json["comment"],
                "date": Input_json["date"],
                "userName": Input_json["userName"]
            }}})
            if x is None:
                return {
                    "msg": "Error Adding Comment, storyId not found",
                    "status": 200
                }
            else:
                return {
                    "msg": "comment added",
                    "status": 200
                }
        except Exception as e:
            return {
                "msg":"problem found in " + str(e),
                "status": 400
            }

    def getAllAvailableTags(self):
        tags = self.tagsCollection.find({}, {"_id": False})
        return {
            "tags":  list(tags),
            "status": 200
        }

    def getAllStories(self, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        totalItems = self.storyCollection.count()
        stories = self.storyCollection.find(projection={
            "_id": False, "comments": False
        }).sort("datePublished", decending).skip(pageNo * 10).limit(10)
        listofStories = []
        for story in stories:
            image = self.userCollection.find_one({"userId": story["userId"]}, projection={
                "_id": False, 'userImage': True, })
            story.update(image)
            listofStories.append(story)
        if (len(listofStories)) == 0:
            return {
                "msg": "no more articles",
                "status": 200
            }
        return {
            "pageNo": pageNo + 1,
            "totalItems": totalItems,
            "items": list(listofStories),
            "status": 200
        }

    def getStoryDetailsByStoryId(self, storyId):
        storyDetails = self.storyCollection.find_one(
            {"storyId": storyId},
            projection={"_id": False}
        )
        if storyDetails:
            return {
                "item": list(storyDetails),
                "status": 200
            }
        else:
            return {
                "msg": "Story not found with " + storyId,
                "status": 200
            }
