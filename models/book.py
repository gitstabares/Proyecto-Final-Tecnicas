from .reservation import Reservation

class Book():
    def __init__(self, title:str, author:str, isbn:int, genre:str, weight:float, price:float):
        self.__title__ = title
        self.__author__ = author
        self.__isbn__ = isbn
        self.__genre__ = genre
        self.__weight__ = weight
        self.__price__ = price
        self.__reservation__ = Reservation()
    def __repr__(self):
        return f"{self.__title__} - {self.__author__}"
    @property
    def title(self):
        return self.__title__
    @title.setter
    def title(self, new_title:str):
        self.__title__ = new_title
    @property
    def author(self):
        return self.__author__
    @author.setter
    def author(self, new_author:str):
        self.__author__ = new_author
    @property
    def isbn(self):
        return self.__isbn__
    @isbn.setter
    def isbn(self, new_isbn:int):
        if new_isbn > 0: self.__isbn__ = new_isbn
    @property
    def genre(self):
        return self.__genre__
    @genre.setter
    def genre(self, new_genre:str):
        self.__genre__ = new_genre
    @property
    def weight(self):   
        return self.__weight__
    @weight.setter
    def weight(self, new_weight:float):
        if new_weight > 0: self.__weight__ = new_weight
    @property
    def price(self):
        return self.__price__
    @price.setter
    def price(self, new_price:float):
        if new_price >= 0: self.__price__ = new_price
    @property
    def reservation(self):
        return self.__reservation__