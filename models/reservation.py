from collections import deque

class Reservation:
    def __init__(self):
        self.__queue__ = deque()
    def pull(self):
        if self.__queue__:
            return self.__queue__.popleft()
        return None
    def push(self, user):
        self.__queue__.append(user)
    def clear(self):
        self.__queue__.clear()