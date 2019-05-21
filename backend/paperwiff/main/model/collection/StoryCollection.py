from mongokat import Collection
from ..document.StoryDocument import StoryDocument
import array
from datetime import datetime
from pymongo import DESCENDING as decending


from paperwiff.main import get_db


class StoryCollection(Collection):
    document_class = StoryDocument
    # Possible filter attributes:: language, views, likes, datePublished, comments
    structure = {
        "comments": array,
        "content": str,
        "copyright": bool,  # Available to the user based on the subscription: Phase 3
        "datePublished": datetime,
        "headerImage": str,
        "language": str,
        "likes": int,
        "storyId": str,
        "storyTitle": str,
        "summary": str,
        "tags": array,
        "userId": str,
        "userName": str,
        "views": int,
        "visibility": str   # Make story Public/Private: Phase 2
    }

    # Methods
    def getAllStories(self, pageNo=1):
        db = get_db()
        userCollection = db['users']


        if pageNo <= 0:
            pageNo = 1
        pageNo = pageNo - 1  # so if page one so that it doesnt skip the first 10 posts
        totalItems = self.count()
        stories = self.find(projection={
            "_id": False, "comments": False
        }).sort("datePublished", decending).skip(pageNo * 10).limit(10)
        listofStories = []
        for story in stories:
            image = userCollection.find_one({"userId": story["userId"]}, projection={
                "_id": False, 'userImage': True, 'firstName': True})
            story.update(image)
            listofStories.append(story)
        if (len(listofStories)) == 0:
            return {
                "msg": "no more articles",
                "items": [],
                "status": 200
            }
        return {
            "pageNo": pageNo + 1,
            "totalItems": totalItems,
            "items": list(listofStories),
            "status": 200
        }
