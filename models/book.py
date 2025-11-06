from ..models import *

class Book():
    def __init__(self, title:str, author:str, isbn:int, genre:str, weight:float, price:float):
        self.__title__ = title
        self.__author__ = author
        self.__isbn__ = isbn
        self.__genre__ = genre
        self.__weight__ = weight
        self.__price__ = price
        self.__reservations__ = Reservation()