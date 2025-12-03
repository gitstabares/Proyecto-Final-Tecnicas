from .reservation import Reservation
from managers.bookManager import BookManager

class Book(object):
    # Builder function
    def __init__(self, title, author, isbn, genre, weight, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.weight = weight
        self.price = price
        self.reservation = Reservation()
        BookManager.addBook(self)
        
    def __repr__(self):
        return f"{self.title} - {self.author}"
    
