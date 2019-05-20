from mongokat import Collection
from ..document.UserDocument import UserDocument
import array

class UserCollection(Collection):
    document_class = UserDocument
    structure = {
        'title': array,
        'body': str,
        'author': str,
        'date_creation': str,
        'rank': int
    }
