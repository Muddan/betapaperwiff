from os.path import dirname, abspath
import os
from flask import json
from mongoengine import connect
from ..model.Tags import Tags


class Datebase:

    def get_db(self):
        db = connect('paperwiff-new')
        self.CreateTags()
        return db

    # Create tags colelction

    def CreateTags(self):
        SITE_ROOT = dirname(dirname(abspath(__file__)))
        json_url = os.path.join(SITE_ROOT, "var/", "availableTags.json")
        data = json.load(open(json_url))
        tags = data['tags']
        if Tags.objects().count() > 0:
            print('Dropping collection..')
            Tags.drop_collection()

        print('Before inserting tag documents')
        print(Tags.objects().count())
        for tag in tags:
            tagStatus = self.str_to_bool(tag['status'])
            Tags(name=tag['name'], tagType=tag['type'], value=tag['value'],
                 status=tagStatus).save()
        print('After inserting tag documents')
        print(Tags.objects().count())
    def str_to_bool(self,s):
        if s == 'True':
            return True
        elif s == 'False':
            return False
        else:
            raise ValueError  # evil ValueError that doesn't tell you what the wrong value was
