from mongoengine import DateTimeField, IntField, ListField, DynamicDocument, StringField, BooleanField
from ..model.Users import Users

class Stories(DynamicDocument):
    # Possible filter attributes:: language, views, likes, datePublished, comments
    comments = ListField(StringField())
    content = StringField()
    copyright = BooleanField(default=False)       # Available to the user based on the subscription: Phase 3
    datePublished = StringField()
    # firstName = StringField()
    headerImage = StringField()
    language = StringField()
    likes = IntField(default=0)
    storyId = StringField()
    storyTitle = StringField()
    summary = StringField()
    tags = ListField(StringField())
    userId = StringField()
    # userImage = StringField()
    # userName = StringField()
    views = IntField(default=1)
    visibility = StringField(default='public')      # Make story public/Private
