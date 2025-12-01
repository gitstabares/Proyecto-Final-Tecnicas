from .reservation import Reservation

class Book():
    # Builder function
    def __init__(self, title, author, isbn, genre, weight, price):
        self.__title__ = title
        self.__author__ = author
        self.__isbn__ = isbn
        self.__genre__ = genre
        self.__weight__ = weight
        self.__price__ = price
        self.__reservation__ = Reservation()
    def __repr__(self):
        return f"{self.__title__} - {self.__author__}"
    # Title's getter and setter
    @property
    def title(self):
        return self.__title__
    @title.setter
    def title(self, new_title):
        self.__title__ = new_title
    # Author's getter and setter
    @property
    def author(self):
        return self.__author__
    @author.setter
    def author(self, new_author):
        self.__author__ = new_author
    # ISBN's getter and setter
    @property
    def isbn(self):
        return self.__isbn__
    @isbn.setter
    def isbn(self, new_isbn):
        if new_isbn > 0: self.__isbn__ = new_isbn
    # Genre's getter and setter
    @property
    def genre(self):
        return self.__genre__
    @genre.setter
    def genre(self, new_genre):
        self.__genre__ = new_genre
    # Weight's getter and setter
    @property
    def weight(self):   
        return self.__weight__
    @weight.setter
    def weight(self, new_weight):
        if new_weight > 0: self.__weight__ = new_weight
    # Price's getter and setter
    @property
    def price(self):
        return self.__price__
    @price.setter
    def price(self, new_price):
        if new_price >= 0: self.__price__ = new_price
    # Queue reservation's getter
    @property
    def reservation(self):
        return self.__reservation__