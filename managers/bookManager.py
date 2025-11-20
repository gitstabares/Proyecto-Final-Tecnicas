from .singleton import _Singleton
from models.book import Book

class BookManager(_Singleton):
    def __init__(self):
        self.__booksByISBN__ = []
        self.__booksByDate__ = []
        self.__inventory__ = {}
    def add(book: Book)