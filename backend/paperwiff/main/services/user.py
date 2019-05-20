from uuid import uuid1

from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, create_refresh_token
from flask import jsonify

from paperwiff.main import get_db

import time
import datetime


class UserClass:
    def __init__(self):
        db = get_db()
        self.userCollection = db['users']

    def userExistsInCollection(self, userId):
        return self.userCollection.find_one({"userId": userId})

    def userNameExistsInCollection(self, userName):
        return self.userCollection.find_one({"userName": userName})

    def getUserDetailsByUserId(self, userId):
        return self.userCollection.find_one(
            {"userId": userId}, {"_id": False})

    def getUserDetailsByuserName(self, userName):
        return self.userCollection.find_one(
            {"userName": userName}, {"_id": False})

    def getUsernameByUserId(self, userId):
        return self.userCollection.find_one({"userId": userId}, projection={
            "_id": False, 'userName': True})

    # Google login
    def createGoogleUser(self, user):
        if self.userExistsInCollection(user['sub']):
            # Login this user, return acess token
            return self.loginGoogleUser(user)
        else:
            userName = '@' + user["given_name"].lower()
            if self.getUserDetailsByuserName(userName) is not None:
                userName = userName + ((str(uuid1())[0:6]))
            # Make the new user object
            newUser = {
                "userId": str(user['sub']),
                "userName": userName,
                "firstName": user["given_name"],
                "lastName": user["family_name"],
                "email": user["email"],
                "accountLicense": "free",
                "followingAuthors": [],
                "followingTags": [],
                "joined": (str(datetime.datetime.now())),
                "about": "",
                "userImage": user['picture'],
                "userArticles": [],
                "likedStories": [],
                "accountLicense": "free",
                "languages": [],
                "location": "",
                "skills": "",
                "saveForLater": []
            }

            try:
                self.userCollection.insert_one(newUser)
                userDetails = self.getUserDetailsByUserId(user['sub'])
                identity = {
                    "userId": user['sub'],
                    "email": user["email"]
                }
                return {
                    "access_token": create_access_token(identity=identity),
                    'refresh_token': create_refresh_token(identity=identity),
                    "userDetails": userDetails,
                    "newUser": True,
                    "status": 200
                }

            except:
                return {
                    "data": 'Error saving user',
                    "status": 400
                }

    # Google login
    def loginGoogleUser(self, user):
        userDetails = self.getUserDetailsByUserId(user['sub'])
        identity = {
            "userId": user['sub'],
            "email": user["email"]
        }
        return {
            "access_token": create_access_token(identity=identity),
            'refresh_token': create_refresh_token(identity=identity),
            "userDetails": userDetails,
            "status": 200
        }

    def FollowTag(self, userId, tag):
        if not self.getUserDetailsByUserId(userId):
            return {
                "msg": "Invalid userId",
                "status": 400
            }

        try:
            if self.userCollection.find_one({"userId": userId, "followingTags": {"$in": [tag]}}):
                self.userCollection.find_one_and_update(
                    {"userId": userId},
                    {"$pull": {"followingTags": {"$in": [tag]}}},
                )
                return {
                    "msg": "Successfully unfollowed the tag",
                    "status": 200
                }

            else:
                self.userCollection.find_one_and_update(
                    {"userId": userId},
                    {"$push": {"followingTags": tag}},
                )
                return {
                    "msg": "Successfully followed the tag",
                    "status": 200
                }

        except Exception as e:
            return {"msg": str(e), "status": 400}

    # update UserDetails
    def updateUserDetails(self, Input):
        userId = Input.get("userId")
        self.userCollection.find_one_and_update(
            {
                "userId": userId
            },

            {
                "$set": {
                    "userName": Input.get("userName"),
                    "firstName": Input.get("firstName"),
                    "lastName": Input.get("lastName"),
                    "about": Input.get("about"),
                    "languages": Input.get("languages"),
                    "location": Input.get("location"),
                    "skills": Input.get("skills"),
                    "availableFor": Input.get("availableFor"),
                }
            }
        )
        return {
            "msg": "successfully updated",
            "status": 200
        }
