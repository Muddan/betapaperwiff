from mongokat import Document

class UserDocument(Document):
    def my_sum(self):
        return self["a"] + self["b"]
