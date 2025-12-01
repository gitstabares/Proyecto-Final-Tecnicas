from .singleton import _Singleton
from models.book import Book
import utils
class BookManager(_Singleton):

    __booksByISBN__ = []
    __booksByDate__ = []
    __stock__ = {}

    @classmethod
    def registerBook(cls,book: Book, quantity: int):
        cls.__booksByISBN__.append(book)
        cls.__booksByDate__.append(book)
        cls.__stock__[book] = quantity
        utils.insertionSort(cls.__booksByISBN__, key=lambda b: b.isbn)

    @classmethod
    def setStock(cls,book: Book, quantity: int):
        cls.__stock__[book] = quantity

    @classmethod
    def lookUpByTitle(cls, title: str):
        return utils.linealSearch(cls.__booksByDate__, title, key=lambda b: b.title)
    
    @classmethod
    def lookUpByAuthor(cls, author: str):
        return utils.linealSearch(cls.__booksByISBN__, author, key=lambda b: b.author)
    
    @classmethod
    def lookUpByISBN(cls, isbn: int):
        return utils.binarySearch(cls.__booksByISBN__, isbn, key=lambda b: b.isbn)