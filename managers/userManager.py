from .singleton import _Singleton
import utils.algorithms as alg

class UserManager(_Singleton):
    usersByName = []
    usersByID = []

    # Registering users' method
    @classmethod
    def addUser(cls,user):
        cls.usersByName.append(user)
        cls.usersByName = alg.insertionSort(cls.usersByName, key=lambda u: u.name)
        cls.usersByID.append(user)
        cls.usersByID = alg.insertionSort(cls.usersByID, key=lambda u: u.userID)

    # Searching users methods
    @classmethod
    def lookUpByName(cls,name):
        return alg.linealSearch(cls.usersByName, name, lambda u: u.name)
    
    @classmethod
    def lookUpByID(cls,userID):
        return alg.binarySearch(cls.usersByID, userID, lambda u: u.userID)