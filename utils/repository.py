from managers.bookManager import BookManager
from managers.userManager import UserManager
from .algorithms import *
from .codec import *

def _saveReport():
    serialize(BookManager.globalReport,'Global Report.json')

def _saveBooks():
    serialize(BookManager.booksByDate,'Books.json')

def _saveStock():
    serialize(BookManager.stock,'Stock.json')

def _saveUsers():
    serialize(UserManager.usersByName,'Users.json')

def saveData():
    '''
    Takes all the static datastructures and dumps them in their JSON files
    '''
    _saveReport()
    _saveBooks()
    _saveStock()
    _saveUsers()

def _loadReport():
    return deserialize('Global Report.json')

def _loadBooks():
    return deserialize('Books.json')

def _loadStock():
    return deserialize('Stock.json')

def _loadUsers():
    return deserialize('Users.json')

def loadData():
    '''
    Loads all the data saved in the data's folder files and dumps it in its respectives datastructures
    '''
    BookManager.globalReport = _loadReport()
    BookManager.booksByDate = _loadBooks()
    BookManager.booksByISBN = insertionSort(BookManager.booksByDate, lambda b: b.isbn)
    BookManager.stock = _loadStock()
    UserManager.usersByName = _loadUsers()
    UserManager.usersByID = insertionSort(UserManager.usersByName, lambda u: u.userID)