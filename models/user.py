from .lendingHistory import LendingHistory
from managers.userManager import UserManager

class User:
    # Builder function
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID
        self.lendingHistory = LendingHistory()
        UserManager.addUser(self)

    def __repr__(self):
        return f"{self.name} - {self.userID}"
    
    def __str__(self):
        return f"{self.name} - {self.userID}"