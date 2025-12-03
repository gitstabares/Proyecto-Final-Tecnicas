from .singleton import _Singleton
import utils.algorithms as alg

class UserManager(_Singleton):
    _usersByName = []
    _usersByID = []

    # Registering users' method
    @classmethod
    def addUser(cls,user):
        cls._usersByName.append(user)
        cls._usersByName = alg.insertionSort(cls._usersByName, key=lambda u: u.name)
        cls._usersByID.append(user)
        cls._usersByID = alg.insertionSort(cls._usersByID, key=lambda u: u.userID)
    
    # List of users ordered by name getter
    @property
    def usersByName(cls):
        return cls._usersByName
    
    # List of users ordered by ID getter
    @property
    def usersByID(cls):
        return cls._usersByID

    # Searching users methods
    @classmethod
    def lookUpByName(cls,name):
        return alg.linealSearch(cls._usersByName, name, lambda u: u.name)
    
    @classmethod
    def lookUpByID(cls,userID):
        return alg.binarySearch(cls._usersByID, userID, lambda u: u.userID)