from .reservation import Reservation
from managers.bookManager import BookManager

class Book(object):
    # Builder function
    def __init__(self, title, author, isbn, genre, weight, price):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._genre = genre
        self._weight = weight
        self._price = price
        self._reservation = Reservation()
        BookManager.addBook(self)
    def __repr__(self):
        return f"{self._title} - {self._author}"
    # Title's getter and setter
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    # Author's getter and setter
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        self._author = author
    # ISBN's getter and setter
    @property
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn(self, isbn):
        if isbn > 0:
            self._isbn = isbn
    # Genre's getter and setter
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, genre):
        self._genre = genre
    # Weight's getter and setter
    @property
    def weight(self):   
        return self._weight
    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self._weight = weight
    # Price's getter and setter
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if price >= 0:
            self._price = price
    # Queue reservation's getter
    @property
    def reservation(self):
        return self._reservation