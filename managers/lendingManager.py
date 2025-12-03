from .singleton import _Singleton
from .bookManager import BookManager

class LendingManager(_Singleton):
    
    @classmethod
    def lendBook(cls, user, book):
        if BookManager.stock[book] > 0:
            user.lendingHistory.push(book)
            BookManager.stock[book] -= 1
        else:
            book.reservation.push(user)

    @classmethod
    def returnBook(cls, book):
        BookManager.stock[book] += 1
        nextUser = book.reservation.pull()
        if nextUser:
            cls.lendBook(nextUser,book)