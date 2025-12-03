import jsonpickle as jp
from managers.bookManager import BookManager
from managers.userManager import UserManager

def serialize(obj, filename):
    with open('data/' + filename,'w') as file:
        file.write(jp.encode(obj, indent=4))
        file.close()

def deserialize(filename):
    with open('data/' + filename,'r') as file:
        output = jp.decode(file.read())
        file.close()
    return output

def saveReport():
    serialize(cls._globalReport,'Global Report.json')
    return cls._globalReport

def saveBooks():
    serialize(._booksByDate,'Books.json')