from collections import deque
from .user import User

class Reservation:
    def __init__(self):
        self.__queue__ = deque()
    def pull(self):
        if self.__queue__:
            return self.__queue__.popleft()
        return None
    def push(self, user:User):
        self.__queue__.append(user)