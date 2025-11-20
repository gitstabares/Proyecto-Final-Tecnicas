from collections import deque
from .book import Book

class LendingHistory():
    def __init__(self):
        self.__isbnStack__ = deque()
        self.__dateStack__ = deque()
    def push(self,book:Book):
        self.__isbnStack__.append(book.__isbn__)
        # Falta la fecha