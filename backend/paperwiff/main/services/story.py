# Utilities Import
from flask import g, json
from datetime import datetime
import re
from uuid import uuid1
from pymongo import DESCENDING as decending
from ..GetDb import get_db

from ..services.user import UserClass

# Model import
from ..model.Stories import Stories
from ..model.Users import Users
from ..helpers.UserServiceHelper import UserServiceHelper
from ..helpers.StoryServiceHelper import StoryServiceHelper
from ..helpers.TagServiceHelper import TagServiceHelper

userService = UserClass()


class StoryClass():

    def __init__(self):
        db = get_db()
        self.storyCollection = db['stories']
        self.tagsCollection = db['tags']
        self.userCollection = db['users']


    # Story CRUD METHODS
    def publishStory(self, userId, tags, storyTitle, content, language,draft, datePublished, headerImage, summary, visibility):
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
                    visibility=visibility,
                    draft=draft,
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
            totalItems = Stories.objects(
                __raw__={"tags": {"$in": [tagName]}}).count()
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

    def deleteByStoryId(self, ArrayOfStoryToDelete):  #make it more secure this api allows any one to delete
        try:
            for storyid in ArrayOfStoryToDelete:
                stry=Stories.objects( storyId = storyid)
                x=json.loads(stry.to_json())
                userId=x[0].get("userId")
                stry.delete()
                print(Users.objects(userId=userId).update_one(pull__userArticles=storyid))
            return {
                "msg":"story has been removed",
                "status":200
            }
        except Exception as e:
            return {
                "msg": "excepton: "+str(e),
                "status": 200
            }




    def getAllStories(self, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        if Stories.objects.count():
            totalItems = Stories.objects.count()
            stories = json.loads(Stories.objects(visibility='public', draft=False).exclude('id', 'comments', 'copyright').order_by(
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
   # user sauthorstories by username

    def getAuthorStories(self, userName, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        if Stories.objects.count():
            totalItems = Stories.objects.count()
            stories = json.loads(Stories.objects(userName=userName).exclude('id', 'comments', 'copyright').order_by(
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
    # user stories by userId


    #get user stories to show to other users
    def getUserStories(self, userId, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        if Stories.objects.count():
            totalItems = Stories.objects.count()
            stories = json.loads(Stories.objects(userId=userId,visibility='public', draft=False).exclude('id', 'comments', 'copyright').order_by(
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

    def getCustomizedStories(self, userId, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        print(userId)
        userData=json.loads(Users.objects(userId=userId,visibility='public', draft=False).to_json())
        UserTags=userData[0].get("followingTags")
        noOfTags=len(UserTags)
        if noOfTags==0:
            return {
                "status": 400,
                "Message":"follow tags that you like to create customized feed"
            }
        numberOfStoryToDisplay=int(10/noOfTags)
        print("no.:"+str(numberOfStoryToDisplay))
        listOfstory=[]
        for tags in UserTags:
            listOfstory+=json.loads(Stories.objects(tags=tags,visibility='public', draft=False).skip(pageNo * 5).limit(5).to_json())
        storyList=[]
        for story in listOfstory:
            if story not in storyList:
                storyList.append(story)
        return {
                "pageNo": pageNo + 1,
                "status": 200,
                "data":storyList

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
                "status": 400
            }


#depricated the below api is depricated

    def getPopularStories(self, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1
        totalItems = Stories.objects().count()
        stories = json.loads(Stories.objects().exclude('id', 'comments', 'copyright').order_by(
            '-views', '-likes').skip(pageNo * 5).limit(5).to_json())
        return {
            "pageNo": pageNo + 1,
            "totalItems": totalItems,
            "items": stories,
            "status": 200
        }

    def getAllPopularStories(self, pageNo=1):

        try:
            if pageNo <= 0:
                pageNo = 1
            pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
            totalItems = self.storyCollection.count()

            stories = self.storyCollection.find(projection={
                "_id": False, "comments": False
            }).skip(pageNo * 10).limit(10).sort("likes",decending).sort("views",decending)
            listofStories = []

            for story in stories:
                print(story)
                image = self.userCollection.find_one({"userId": story["userId"]}, projection={
                    "_id": False, 'userImage': True, })
                story.update(image)
                listofStories.append(story)
            if (len(listofStories)) == 0:
                return {
                    "msg": "no more stories",
                    "status": 200
                }
            return {
                "pageNo": pageNo + 1,
                "totalItems": totalItems,
                "items": list(listofStories),
                "status": 200
            }
        except Exception as e:
            return {
                "excetion":str(e),
                "status": 400
            }



    def deleteByStoryId(self, storyId):
        if not StoryServiceHelper().storyIdExists(storyId):
            return {
                "msg": "The storyId does not exists, please try again",
                "status": 400
            }

        userId = Stories.objects(storyId=storyId).first().userId

        if not UserServiceHelper().userIdExists(userId):
            return {
                "msg": "Story contains invalid userId, please try again",
                "status": 200
            }
        print('Deleting story with storyId ' + storyId)
        try:
            Stories.objects(storyId=storyId).delete()

            print('Removing story details from userId ' + userId)
            Users.objects(userId=userId).update_one(
                pull__userArticles=storyId)
            Users.objects(userId=userId).update_one(
                pull__saveForLater=storyId)
            return {
                "msg": "story has been deleted successfully",
                "status": 200
            }
        except Exception as e:
            return {
                "msg": "excepton: "+str(e),
                "status": 200
            }

    def updateStoryDetails(self,Input):
        storyId = Input.get("storyId")
        if StoryServiceHelper.storyIdExists(self,storyId):
            storyTitle=Input.get("storyTitle")

            Stories.objects(storyId=storyId).update_one(
                set__content=Input.get("content"),
                set__language=Input.get("language"),
                set__storyTitle=Input.get("storyTitle"),
                set__summary=Input.get("summary"),
                set__tags=Input.get("tags"),
                set__headerImage = Input.get("headerImage"),
                set__visibility = Input.get("visibility"),  #public or Private
                #set__storyId = re.sub('[^A-Za-z0-9-"-"]+', '',storyTitle.lower().replace(" ", "-"))

            )
            return {
                "msg": "successfully updated",
                "status": 200
            }
        else:
            return {
                "msg": "storyId does not exists, please try with valid storyId ",
                "status": 200
            }