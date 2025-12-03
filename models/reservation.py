from collections import deque

class Reservation:
    # Builder function
    def __init__(self):
        self._queue = deque()
    # Push and pull function for queue
    def push(self, user):
        self._queue.append(user)
    def pull(self):
        if self._queue:
            return self._queue.popleft()
        return None
    # Function to clear all the queue
    def clear(self):
        self._queue.clear()