from mongoengine import DateTimeField, IntField, ListField, Document, StringField, BooleanField, MapField


class Users(Document):
    about = StringField(default='')
    availableFor = StringField(default="")
    accountLicense = StringField(default="free")
    email = StringField(default='')
    singInProvider=StringField(default='')
    firstName =StringField(default='')
    followingAuthors = ListField(StringField())
    followingTags = ListField(StringField())
    joined = DateTimeField()
    languages = ListField(StringField())
    lastName = StringField(default='')
    likedStories = ListField(StringField())
    location = StringField(default='')
    saveForLater = ListField(StringField())
    skills = StringField(default='')
    userArticles = ListField(StringField())
    userId = StringField(default='')
    userImage = StringField(default='')
    userName = StringField(default='')
