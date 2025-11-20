from models.book import Book

def insertionSort(array:list,key:callable)->list:
    for i in range(1, len(array)):
        actual = array[i]
        j = i - 1
        while j >= 0 and key(actual) < key(array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = actual
    return array

libros = [Book("Cien Años de Soledad", "Gabriel García Márquez",4651654,"Fiction", 5, 50000),
          Book("Don Quijote de la Mancha", "Miguel de Cervantes", 9788491050293,"Fiction", 4.5, 45000),
          Book("La Sombra del Viento", "Carlos Ruiz Zafón", 9788408130424,"Mystery", 3.2, 40000),
          Book("El Amor en los Tiempos del Cólera", "Gabriel García Márquez", 9780307389732,"Romance", 4.0, 48000),
          Book("1984", "George Orwell", 9780451524935,"Dystopian", 2.5, 35000)]

sorted_libros = insertionSort(libros, key=lambda book: book.__title__)
print([libro.__title__ for libro in sorted_libros])