from ..model.Stories import Stories
from ..model.Tags import Tags
from flask import json

class StoryServiceHelper():

    def storyIdExists(self, storyId):
        if Stories.objects(storyId=storyId):
            return True
        else:
            return False
    def getAvailableTags(self):
        return Tags.objects().exclude('id').to_json()

    def getStoryDetailsByStoryId(self, storyId):
        return Stories.objects(storyId=storyId).exclude('id').first()
