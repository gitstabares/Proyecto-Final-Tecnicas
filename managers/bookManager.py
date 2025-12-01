from .singleton import _Singleton
import utils.algorithms as alg

class BookManager(_Singleton):
    
    __booksByDate__ = []
    __booksByISBN__ = []
    __stock__ = {}

    @classmethod
    def addBook(cls,book, quantity):
        cls.__booksByISBN__.append(book)
        cls.__booksByDate__.append(book)
        cls.__stock__[book] = quantity
        alg.insertionSort(cls.__booksByISBN__, key=lambda b: b.isbn)

    @classmethod
    def setStock(cls,book, quantity):
        cls.__stock__[book] = quantity

    @classmethod
    def lookUpByTitle(cls, title):
        return alg.linealSearch(cls.__booksByDate__, title, key=lambda b: b.title)
    
    @classmethod
    def lookUpByAuthor(cls, author):
        return alg.linealSearch(cls.__booksByISBN__, author, key=lambda b: b.author)
    
    @classmethod
    def lookUpByISBN(cls, isbn):
        return alg.binarySearch(cls.__booksByISBN__, isbn, key=lambda b: b.isbn)