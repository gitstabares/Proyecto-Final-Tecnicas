from .lendingHistory import LendingHistory

class User:
    def __init__(self, name:str, id:int, LendingHistory:LendingHistory):
        self.__name__ = name
        self.__id__ = id
        self.__lendingHistory__ = LendingHistory
    @property
    def name(self):
        return self.__name__
    @property
    def id(self):
        return self.__id__
    @property
    def lendingHistory(self):
        return self.__lendingHistory__