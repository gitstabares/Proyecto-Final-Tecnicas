from collections import deque
from datetime import date

class LendingHistory():
    # Builder function
    def __init__(self):
        self._isbnStack = deque()
        self._dateStack = deque()
    # Push and pull function for stack
    def push(self,book):
        self._isbnStack.append(book.isbn)
        self._dateStack.append(date.today())
    def pull(self):
        if self._isbnStack and self._dateStack:
            return (self._isbnStack.pop(), self._dateStack.pop())
        return None
    # Function to clear all the stack
    def clear(self):
        self._isbnStack.clear()
        self._dateStack.clear()