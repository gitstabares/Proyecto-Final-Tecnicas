from .singleton import _Singleton
from .bookManager import BookManager

class LendingManager(_Singleton):
    
    @classmethod
    def lendBook(cls, user, book):
        '''
        Lends a book to the user
        Args:
            user(User): User who wants borrow a book
            book(Book): Book to be lent
        '''
        # If there's stock the book is lent
        if BookManager.stock[book] > 0:
            user.lendingHistory.push(book)
            BookManager.stock[book] -= 1
        # Else, add the user to the book's waiting list
        else:
            book.reservation.push(user)

    @classmethod
    def returnBook(cls, book):
        '''
        Return a lent book to the library
        Args:
            book(Book): Book to be lent
        '''        
        BookManager.stock[book] += 1
        nextUser = book.reservation.pull()
        # If there's someone in the waiting list after the book is returned, then it can be lent again
        if nextUser:
            cls.lendBook(nextUser,book)