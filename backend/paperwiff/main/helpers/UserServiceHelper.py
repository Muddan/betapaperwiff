
from ..model.Users import Users
from flask import json


class UserServiceHelper:

    def userNameExists(self, userName):
        if Users.objects(userName=userName):
            return True
        else:
            return False

    def userIdExists(self, userId):
        if Users.objects(userId=userId):
            return True
        else:
            return False

    def getUserDetailsByUserName(self, userName):
        return Users.objects(userName=userName).exclude('id')

    def getUserDetailsByUserId(self, userId):
        return Users.objects(userId=userId).exclude('id')

    def getAuthorDetailsByName(sefl, userName):
        return Users.objects(userName=userName).exclude(
            'id',
            'accountLicense',
            'singInProvider',
            'followingTags',
            'likedStories',
            'saveForLater',
            'userArticles'
        )

    def getAuthorDetailsById(sefl, userId):
        return Users.objects(userId=userId).exclude(
            'id',
            'accountLicense',
            'singInProvider',
            'followingTags',
            'likedStories',
            'saveForLater',
            'userArticles'
        )