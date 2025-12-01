from collections import deque

class Reservation:
    # Builder function
    def __init__(self):
        self.__queue__ = deque()
    # Push and pull function for queue
    def push(self, user):
        self.__queue__.append(user)
    def pull(self):
        if self.__queue__:
            return self.__queue__.popleft()
        return None
    # Function to clear all the queue
    def clear(self):
        self.__queue__.clear()