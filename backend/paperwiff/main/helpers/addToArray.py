from paperwiff.main import get_db

def addToArrayUser(MongoDbFieldName,Value,userId):
    db = get_db()
    userCollection = db['users']
    print(userId,Value,MongoDbFieldName)
    try:

        x=userCollection.update(
            {"userId": userId},
            {"$pull": {MongoDbFieldName: {"$in": [Value]}}},
        )

        if x["nModified"]==0:
            userCollection.find_one_and_update(
                {"userId": userId},
                {"$push": {MongoDbFieldName: Value}}
            )
            return {
                "msg": "Successfully added",
                "status": 200
            }
        return {
            "msg": "Successfully removed",
            "status": 200
        }



    except Exception as e:
            return {
                "msg": "problem occured :"+ str(e),
                "status": 200
            }



def addToArrayStory(MongoDbFieldName,Value,storyId):
    db = get_db()
    userCollection = db['stories']
    print(storyId,Value,MongoDbFieldName)
    try:

        x=userCollection.update(
            {"storyId": storyId},
            {"$pull": {MongoDbFieldName: {"$in": [Value]}}},
        )

        if x["nModified"]==0:
            userCollection.find_one_and_update(
                {"storyId": storyId},
                {"$push": {MongoDbFieldName: Value}}
            )
            return {
                "msg": "Successfully added",
                "status": 200
            }
        return {
            "msg": "Successfully removed",
            "status": 200
        }
    except Exception as e:
            return {
                "msg": "problem occured :"+ str(e),
                "status": 200
            }
