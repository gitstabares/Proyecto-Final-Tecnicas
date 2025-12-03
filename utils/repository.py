from managers.bookManager import BookManager
from managers.userManager import UserManager
from .codec import *

def saveReport():
    serialize(BookManager.globalReport,'Global Report.json')

def saveBooks():
    serialize(BookManager.booksByDate,'Books.json')

def saveStock():
    serialize(BookManager.stock,'Stock.json')

def saveUsers():
    serialize(UserManager.usersByName,'Users.json')