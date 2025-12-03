from .singleton import _Singleton
import utils.algorithms as alg
from utils.codec import *

class BookManager(_Singleton):
    
    booksByDate = []
    booksByISBN = []
    globalReport = []
    stock = {}

    # Register book
    @classmethod
    def addBook(cls,book, quantity = 1):
        cls.booksByISBN.append(book)
        cls.booksByDate.append(book)
        cls.globalReport.append(book)
        cls.stock[book.isbn] = quantity
        cls.booksByISBN = alg.insertionSort(cls.booksByISBN, key=lambda b: b.isbn)
        cls.globalReport = alg.mergeSort(cls.globalReport, key=lambda b: b.price)

    # Delete book from lists
    @classmethod
    def removeBook(cls,book):
        if book in cls.booksByISBN:
            cls.booksByISBN.remove(book)
        if book in cls.booksByDate:
            cls.booksByDate.remove(book)
        if book in cls.globalReport:
            cls.globalReport.remove(book)
        if str(book) in cls.stock.keys():
            del cls.stock[str(book)]

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
    
    # Generate global report
    @classmethod
    def generateReport(cls):
        serialize(cls.globalReport,'Global Report.json')
        return cls.globalReport
    
    # Recursive function to calculate the total price of a list of books written by given author
    def totalPrice(author):
        books = [b for b in BookManager.booksByDate if b.author == author]
        return alg.recursiveAddition(books, lambda b:b.price)
    
    # Recursive function to calculate the total price of a list of books written by given author
    def meanWeight(author):
        books = [b for b in BookManager.booksByDate if b.author == author]
        return alg.recursiveMean(books, lambda b:b.weight)