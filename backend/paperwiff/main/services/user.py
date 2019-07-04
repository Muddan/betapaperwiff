import datetime
import time
from uuid import uuid1

from flask import jsonify, json
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_required)


from ..model.Users import Users
from ..model.Stories import Stories

# Helpers
from ..helpers.UserServiceHelper import UserServiceHelper
from ..helpers.StoryServiceHelper import StoryServiceHelper

# Firebase initialization
import firebase_admin
from firebase_admin import auth


class UserClass(UserServiceHelper, StoryServiceHelper):

    def __init__(self):
        pass
    # update UserDetails

    def updateUserDetails(self, Input):
        userId = Input.get("userId")
        if self.userIdExists(userId):
            if(Input['userImage']):
                Users.objects(userId=userId).update_one(
                    set__userImage=Input.get("userImage"),
                )
            Users.objects(userId=userId).update_one(
                set__about=Input.get("about"),
                set__email=Input.get("email"),
                set__firstName=Input.get("firstName"),
                set__languages=Input.get("languages"),
                set__lastName=Input.get("lastName"),
                set__location=Input.get("location"),
                set__skills=Input.get("skills"),
            )
            return {
                "msg": "successfully updated",
                "status": 200
            }
        else:
            return {
                "msg": "userId does not exists, please try again",
                "status": 200
            }

    # Retrevies user data from IdToken sent from firebase, create new user.
    def firebaseUser(self, id_token, fullName):
        decoded = auth.verify_id_token(id_token)

        if decoded['firebase']['sign_in_provider'] == 'password':

            if fullName:
                # Check if username already exixts, email will be unique from firebase authentication
                userName = '@' + fullName.split(' ')[0].lower()
                if self.userNameExists(userName):
                    userName = userName + ((str(uuid1())[0:6]))
                user = Users(
                    firstName=fullName,
                    joined=str(datetime.datetime.now()),
                    userId=decoded['user_id'],
                    email=decoded['email'],
                    userName=userName,
                    singInProvider=decoded['firebase']['sign_in_provider']
                )
                user.save()
                currentUser = self.getUserDetailsByUserId(
                    decoded['user_id']).first()
                identity = {
                    "userId": currentUser.userId,
                    "email": currentUser.email
                }
                return {
                    "access_token": create_access_token(identity=identity),
                    'refresh_token': create_refresh_token(identity=identity),
                    "social_login": False,
                    "userDetails": json.loads(currentUser.to_json()),
                    "status": 200
                }
            else:
                return {
                    "msg": 'FullName is missing, please enter and try again',
                    "status": 400
                }

        else:
            if not self.userIdExists(decoded['user_id']):

                # Check if username already exixts, email will be unique from firebase authentication
                userName = '@' + decoded["name"].split(' ')[0].lower()
                if self.userNameExists(userName):
                    userName = userName + ((str(uuid1())[0:6]))
                user = Users(
                    firstName=decoded['name'],
                    joined=str(datetime.datetime.now()),
                    userId=decoded['user_id'],
                    userImage=decoded['picture'],
                    email=decoded['email'],
                    userName=userName,
                    singInProvider=decoded['firebase']['sign_in_provider']
                )
                user.save()
            currentUser = self.getUserDetailsByUserId(
                decoded['user_id']).first()
            identity = {
                "userId": currentUser.userId,
                "email": currentUser.email
            }
            return {
                "access_token": create_access_token(identity=identity),
                'refresh_token': create_refresh_token(identity=identity),
                "social_login": False,
                "userDetails": json.loads(currentUser.to_json()),
                "status": 200
            }

    def firebaseEmailUser(self, userId):
        currentUser = self.getUserDetailsByUserId(userId).first()
        identity = {
            "userId": currentUser.userId,
            "email": currentUser.email
        }
        return {
            "access_token": create_access_token(identity=identity),
            'refresh_token': create_refresh_token(identity=identity),
            "social_login": False,
            "userDetails": json.loads(currentUser.to_json()),
            "status": 200
        }

    # SOCIAL FEATURES

    # Follow Tags; takes an Array of tags[] and userId
    def followTags(self, userId, tags):
        try:
            if Users.objects(__raw__={"userId": userId, "followingTags": {"$in": tags}}):
                Users.objects(userId=userId).update_one(
                    pull_all__followingTags=tags)
                return {
                    "msg": "Successfully unfollowed the tags",
                    "status": 200
                }

            else:
                Users.objects(userId=userId).update_one(
                    push_all__followingTags=tags)
                return {
                    "msg": "Successfully followed the tags",
                    "status": 200
                }

        except Exception as e:
            return {"msg": str(e), "status": 400}

    def followAuthor(self, userId, authorId):
        # TODO Check if author Id exists
        if UserServiceHelper().userIdExists(authorId) and UserServiceHelper().userIdExists(userId):
            if Users.objects(__raw__={"userId": userId, "followingAuthors": {"$in": [authorId]}}):
                Users.objects(userId=userId).update_one(
                    pull__followingAuthors=authorId)
                return {
                    "msg": "Successfully unfollowed the Author",
                    "status": 200
                }

            else:
                Users.objects(userId=userId).update_one(
                    push__followingAuthors=authorId)
                return {
                    "msg": "Successfully followed the Author",
                    "status": 200
                }
        else:
            return {
                "msg": "Invalid userId and authorId, please try again",
                "status": 200
            }

    # Single Value storyId
    def storyLikes(self, userId, storyId):
        if UserServiceHelper().userIdExists(userId) and StoryServiceHelper().storyIdExists(storyId):
            if Users.objects(__raw__={"userId": userId, "likedStories": {"$in": [storyId]}}):
                Users.objects(userId=userId).update_one(
                    pull__likedStories=storyId)
                Stories.objects(storyId=storyId).update_one(dec__likes=1)
                return {
                    "msg": "Successfully unliked",
                    "status": 200
                }
            else:
                Users.objects(userId=userId).update_one(
                    push__likedStories=storyId)
                Stories.objects(storyId=storyId).update_one(inc__likes=1)
                return {
                    "msg": "Successfully liked",
                    "status": 200
                }
        else:
            return {
                "msg": "No story with that storyId",
                "status": 200
            }

    def storySave(self, userId, storyId):
        if UserServiceHelper().userIdExists(userId) and StoryServiceHelper().storyIdExists(storyId):
            if Users.objects(__raw__={"userId": userId, "saveForLater": {"$in": [storyId]}}):
                Users.objects(userId=userId).update_one(
                    pull__saveForLater=storyId)
                return {
                    "msg": "Successfully removed from saved list",
                    "status": 200
                }
            else:
                Users.objects(userId=userId).update_one(
                    push__saveForLater=storyId)
                return {
                    "msg": "Successfully added to saved list",
                    "status": 200
                }
        else:
            return {
                "msg": "No storyId exist",
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
                "msg": "problem found in " + str(e),
                "status": 400
            }

    def getUserSavedStories(self, userId):
        savedList = list(self.getUserDetailsByUserId(
            userId).first().saveForLater)
        savedStories = []
        for savedStory in savedList:
            savedStories.append(json.loads(
                self.getStoryDetailsByStoryId(savedStory).to_json()))
        return {
            "items": savedStories,
            "total_items": len(savedStories),
            "status": 200
        }

    def getAuthorDetails(self, authorId):
        details = json.loads(
            self.getAuthorDetailsByName(authorId).first().to_json())
        return {
            "details": details,
            "status": 200
        }

    def getCustomizedStories(self, userId, pageNo=1):
        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        userData = json.loads(Users.objects(userId=userId).to_json())
        UserTags = userData[0].get("followingTags")
        noOfTags = len(UserTags)
        if noOfTags == 0:
            return {
                "status": 400,
                "Message": "follow tags that you like to create customized feed"
            }
        numberOfStoryToDisplay = int(10/noOfTags)
        listOfstory = []
        for tags in UserTags:
            listOfstory += json.loads(Stories.objects(
                tags=tags).exclude('id').skip(pageNo * 10).limit(10).to_json())
        storyList = []
        for story in listOfstory:
            if story not in storyList:
                storyList.append(story)
        return {
            "pageNo": pageNo + 1,
            "status": 200,
            "items": storyList
        }
