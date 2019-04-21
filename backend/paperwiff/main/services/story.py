from flask import g
import datetime
from paperwiff.main import get_db
from pymongo import DESCENDING as decending
from ..services.user import UserClass


userService = UserClass()


class StoryClass:
    def __init__(self):
        db = get_db()
        self.storyCollection = db['stories']
        self.tagsCollection = db['tags']

    def publishStory(self, userId, tags, storyTitle, content):
        userName = userService.getUsernameByUserId(userId)
        newStory = {
            "storyId": storyTitle.lower().replace(" ", "-"),
            "userId": userId,
            "userName": userName["userName"],
            "storyTitle": storyTitle,
            "content": content,
            "tags": tags,
            "likes": 0,
            "datePublished": (str(datetime.datetime.now()))
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

    def getAllAvailableTags(self):
        tags = self.tagsCollection.find({}, {"_id": False})
        return list(tags)

    def getAllStories(self):
        stories = self.storyCollection.find(projection={
            "_id": False
        }).limit(10).sort("datePublished", decending)
        return list(stories)

    def getStoryDetailsByStoryId(self, storyId):
        storyDetails = self.storyCollection.find(
            {"storyId": storyId},
            projection={"_id": False}
        )
        return list(storyDetails)
