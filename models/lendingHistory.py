from collections import deque
from datetime import date

class LendingHistory():
    def __init__(self):
        self.__isbnStack__ = deque()
        self.__dateStack__ = deque()
    def push(self,book):
        self.__isbnStack__.append(book.isbn)
        self.__dateStack__.append(date.today())
    def pull(self):
        if self.__isbnStack__ and self.__dateStack__:
            return (self.__isbnStack__.pop(), self.__dateStack__.pop())
        return None
    def clear(self):
        self.__isbnStack__.clear()
        self.__dateStack__.clear()