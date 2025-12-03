from managers.bookManager import BookManager
from managers.userManager import UserManager
from .algorithms import *
from .codec import *

def saveReport():
    serialize(BookManager.globalReport,'Global Report.json')

def saveBooks():
    serialize(BookManager.booksByDate,'Books.json')

def saveStock():
    serialize(BookManager.stock,'Stock.json')

def saveUsers():
    serialize(UserManager.usersByName,'Users.json')

def saveData():
    saveReport()
    saveBooks()
    saveStock()
    saveUsers()

def loadReport():
    return deserialize('Global Report.json')

def loadBooks():
    return deserialize('Books.json')

def loadStock():
    return deserialize('Stock.json')

def loadUsers():
    return deserialize('Users.json')

def loadData():
    BookManager.globalReport = loadReport()
    BookManager.booksByDate = loadBooks()
    BookManager.booksByISBN = insertionSort(BookManager.booksByDate, lambda b: b.isbn)
    BookManager.stock = loadStock()
    UserManager.usersByName = loadUsers()
    UserManager.usersByID = insertionSort(UserManager.usersByName, lambda u: u.userID)