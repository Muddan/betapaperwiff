from ..model.Tags import Tags
from flask import json


class TagServiceHelper():

    def isValid(self, value):
        if Tags.objects(value=value):
            return True
        else:
            return False
