from .lendingHistory import LendingHistory

class User:
    # Builder function
    def __init__(self, name, id, lendingHistory):
        self.__name__ = name
        self.__id__ = id
        self.__lendingHistory__ = LendingHistory()
    # Name's getter and setter
    @property
    def name(self):
        return self.__name__
    @name.setter
    def name(self, new_name):
        self.__name__ = new_name
    # ID's getter
    @property
    def id(self):
        return self.__id__
    # Lending history's getter
    @property
    def lendingHistory(self):
        return self.__lendingHistory__