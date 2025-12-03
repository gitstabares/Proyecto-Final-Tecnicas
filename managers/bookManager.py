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
    
    # Stack's recursive method
    @classmethod
    def totalValue(cls, author, books = booksByDate):
        # Base case: there's one last remaining element
        if len(books) == 0:
            return 0
        
        # Recursive call
        if books[0].author == author:
            return books[0].price + cls.totalValue(author, books[1:])
        return cls.totalValue(author, books[1:])
    
    # Tail's recursive method
    @classmethod
    def meanWeight(cls, author, index=0, total_weight=0, count=0):

        print(f"Recursive call: index={index}, total_weight={total_weight}, count={count}")

        # Base case: Booklist finished
        if index == len(cls.booksByDate):
            if count == 0:
                return 0  # There's no books of this author
            return total_weight / count

        # If there are books of the author, add them
        if cls.booksByDate[index].author == author:
            new_total = total_weight + cls.booksByDate[index].weight
            new_count = count + 1
        else:
            new_total = total_weight
            new_count = count

        # Next recursive call
        return cls.meanWeight(
            author,
            index + 1,
            new_total,
            new_count
        )