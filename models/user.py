from ..models import *

class User:
    def __init__(self, name:str, id:int, LendingHistory:LendingHistory):
        self.__name__ = name
        self.__id__ = id
        self.__lendingHistory__ = LendingHistory
    @property
    def lendingHistory(self):
        return self.__lendingHistory__