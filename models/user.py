from .lendingHistory import LendingHistory
from managers.userManager import UserManager

class User:
    # Builder function
    def __init__(self, name, userID):
        self._name = name
        self._userID = userID
        self._lendingHistory = LendingHistory()
        UserManager.addUser(self)
    # Name's getter and setter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name
    # ID's getter
    @property
    def userID(self):
        return self._userID
    # Lending history's getter
    @property
    def lendingHistory(self):
        return self._lendingHistory