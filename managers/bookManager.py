from .singleton import _Singleton
import utils.algorithms as alg
from utils.codec import *

class BookManager(_Singleton):
    
    _booksByDate = []
    _booksByISBN = []
    _globalReport = []
    _stock = {}

    # Books' registering method
    @classmethod
    def addBook(cls,book, quantity = 1):
        cls._booksByISBN.append(book)
        cls._booksByDate.append(book)
        cls._globalReport.append(book)
        cls._stock[book] = quantity
        cls._booksByISBN = alg.insertionSort(cls._booksByISBN, key=lambda b: b.isbn)
        cls._globalReport = alg.mergeSort(cls._globalReport, key=lambda b: b.price)

    # Stock's getter and setter
    @property
    def stock(cls):
        return cls._stock

    @classmethod
    def setStock(cls,book, quantity):
        cls._stock[book] = quantity

    # Book's list ordered by date getter
    @property
    def booksByDate(cls):
        return cls._booksByDate
    
    # Book's list ordered by ISBN getter
    @property
    def booksByISBN(cls):
        return cls._booksByISBN
    
    # Global report's getter
    @property
    def globalReport(cls):
        return cls._globalReport

    # Searching books methods
    @classmethod
    def lookUpByTitle(cls, title):
        return alg.linealSearch(cls._booksByDate, title, key=lambda b: b.title)
    
    @classmethod
    def lookUpByAuthor(cls, author):
        return alg.linealSearch(cls._booksByISBN, author, key=lambda b: b.author)
    
    @classmethod
    def lookUpByISBN(cls, isbn):
        return alg.binarySearch(cls._booksByISBN, isbn, key=lambda b: b.isbn)