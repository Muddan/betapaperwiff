from mongoengine import ListField, DynamicDocument, StringField, BooleanField

class Tags(DynamicDocument):
    name = StringField()
    tagType = StringField()
    status = BooleanField()
