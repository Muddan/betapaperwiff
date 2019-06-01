# Utilities Import
from flask import g, json
from datetime import datetime
import re
from uuid import uuid1
from pymongo import DESCENDING as decending

from ..services.user import UserClass

# Model import
from ..model.Stories import Stories
from ..helpers.UserServiceHelper import UserServiceHelper
from ..helpers.StoryServiceHelper import StoryServiceHelper
from ..helpers.TagServiceHelper import TagServiceHelper

userService = UserClass()


class StoryClass():

    def __init__(self):
        pass

    # Story CRUD METHODS
    def publishStory(self, userId, tags, storyTitle, content, language, datePublished, headerImage, summary):
        userData = UserServiceHelper().getUserDetailsByUserId(userId)
        for tag in tags:
            if not TagServiceHelper().isValid(tag):
                return {
                    "msg": "Invalid Tag value",
                    "status": 400
                }
            else:
                continue
        try:
            if userData:
                storyId = re.sub('[^A-Za-z0-9-"-"]+', '',
                                 storyTitle.lower().replace(" ", "-"))
                result = Stories.objects(storyId=storyId)
                if result:
                    storyId = storyId+((str(uuid1())[0:6]))
                story = Stories(
                    content=content,
                    datePublished=(str(datetime.now())),
                    headerImage=headerImage,
                    language=language,
                    storyId=storyId,
                    storyTitle=storyTitle,
                    summary=summary,
                    tags=tags,
                    userId=userId,
                    userName=userData.first().userName,
                    firstName=userData.first().firstName,
                    userImage=userData.first().userImage,
                )
                story.save()
                userData.update_one(push__userArticles=storyId)
                return {
                    "msg": 'Saved the story',
                    "status": 200
                }
            else:
                return {
                    "msg": "Invalid userId",
                    "status": 400
                }
        except Exception as e:
            return {
                "msg": "Error occurred saving story" + str(e),
                "status": 200
            }

    def getAllAvailableTags(self):
        tags = StoryServiceHelper().getAvailableTags()
        return {
            "tags":  json.loads(tags),
            "status": 200
        }

    def getTagStories(self, tagName, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        if Stories.objects(__raw__={"tags": {"$in": [tagName]}}).count():
            totalItems = Stories.objects(__raw__={"tags": {"$in": [tagName]}}).count()
            stories = json.loads(Stories.objects(__raw__={"tags": {"$in": [tagName]}}).exclude('id', 'comments', 'copyright').order_by(
                '-datePublished', ).skip(pageNo * 10).limit(10).to_json())

            return {
                "pageNo": pageNo + 1,
                "totalItems": totalItems,
                "items": stories,
                "status": 200
            }
        else:
            return {
                "msg": "Sorry, no articles are available",
                "items": [],
                "status": 200
            }

    def getAllStories(self, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        if Stories.objects.count():
            totalItems = Stories.objects.count()
            stories = json.loads(Stories.objects().exclude('id', 'comments', 'copyright').order_by(
                '-datePublished', ).skip(pageNo * 10).limit(10).to_json())

            return {
                "pageNo": pageNo + 1,
                "totalItems": totalItems,
                "items": stories,
                "status": 200
            }
        else:
            return {
                "msg": "Sorry, no articles are available",
                "items": [],
                "status": 200
            }

    def getUserStories(self, userName, pageNo=1):
        listofStories = []
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        totalItems = self.storyCollection.count()

        stories = self.storyCollection.find({"userName": userName},
                                            projection={
            "_id": False, "comments": False
        }).sort("datePublished", decending).skip(pageNo * 10).limit(10)
        for story in stories:
            image = self.userCollection.find_one({"userName": story["userName"]}, projection={
                "_id": False, 'userImage': True})
            story.update(image)
            listofStories.append(story)
        if (len(listofStories)) == 0:
            return {
                "msg": "no story by User found",
                "items": [],
                "status": 200
            }

        return {
            "pageNo": pageNo + 1,
            "totalItems": totalItems,
            "items": list(listofStories),
            "status": 200
        }

    # Send story details when story url is visited
    def getStoryDetailsByStoryId(self, storyId):
        Stories.objects(storyId=storyId).update_one(inc__views=1)
        storyDetails = json.loads(Stories.objects(
            storyId=storyId).exclude('id').first().to_json())
        if storyDetails:
            return {
                "item": storyDetails,
                "status": 200
            }
        else:
            return {
                "msg": "Story not found with " + storyId,
                "status": 200
            }
