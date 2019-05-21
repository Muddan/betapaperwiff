from mongokat import Document

class StoryDocument(Document):
    def my_sum(self):
        return self["a"] + self["b"]
