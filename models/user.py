class User:
    def __init__(self, name:str, id:int, lendingHistory):
        self.__name__ = name
        self.__id__ = id
        self.__lendingHistory__ = lendingHistory
    @property
    def name(self):
        return self.__name__
    @name.setter
    def name(self, new_name:str):
        self.__name__ = new_name
    @property
    def id(self):
        return self.__id__
    @id.setter
    def id(self, new_id:int):
        if new_id > 0: self.__id__ = new_id
    @property
    def lendingHistory(self):
        return self.__lendingHistory__