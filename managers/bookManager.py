from .singleton import _Singleton
import utils.algorithms as alg
from utils.codec import *

class BookManager(_Singleton):
    
    booksByDate = []
    booksByISBN = []
    globalReport = []
    stock = {}

    # Registering book method
    @classmethod
    def addBook(cls,book, quantity = 1):
        cls.booksByISBN.append(book)
        cls.booksByDate.append(book)
        cls.globalReport.append(book)
        cls.stock[book] = quantity
        cls.booksByISBN = alg.insertionSort(cls.booksByISBN, key=lambda b: b.isbn)
        cls.globalReport = alg.mergeSort(cls.globalReport, key=lambda b: b.price)

    # Stock's setter
    @classmethod
    def setStock(cls,book, quantity):
        cls.stock[book] = quantity

    # Searching books methods
    @classmethod
    def lookUpByTitle(cls, title):
        return alg.linealSearch(cls.booksByDate, title, key=lambda b: b.title)
    
    @classmethod
    def lookUpByAuthor(cls, author):
        return alg.linealSearch(cls.booksByDate, author, key=lambda b: b.author)
    
    @classmethod
    def lookUpByISBN(cls, isbn):
        return alg.binarySearch(cls.booksByISBN, isbn, key=lambda b: b.isbn)
    
    # Method for generate global report
    @classmethod
    def generateReport(cls):
        serialize(cls.globalReport,'Global Report.json')
        return cls.globalReport