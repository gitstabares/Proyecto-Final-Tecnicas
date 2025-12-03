from PyQt6.QtWidgets import (
    QWidget, QFormLayout, QLineEdit, QPushButton,
    QMessageBox, QListWidget, QComboBox, QVBoxLayout,
    QLabel
)
from PyQt6.QtCore import Qt
from models.book import Book
from managers.bookManager import BookManager

class BookMenuActions:

    def addBook(self):
        """Displays a form to add a new book."""

        form = QWidget()
        layout = QFormLayout()

        self.titleInput = QLineEdit()
        self.authorInput = QLineEdit()
        self.isbnInput = QLineEdit()
        self.genreInput = QLineEdit()
        self.weightInput = QLineEdit()
        self.valueInput = QLineEdit()

        layout.addRow("Title:", self.titleInput)
        layout.addRow("Author:", self.authorInput)
        layout.addRow("ISBN:", self.isbnInput)
        layout.addRow("Genre:", self.genreInput)
        layout.addRow("Weight:", self.weightInput)
        layout.addRow("Value:", self.valueInput)

        registerBtn = QPushButton("Register Book")
        registerBtn.clicked.connect(self._registerBook)

        layout.addRow(registerBtn)

        form.setLayout(layout)
        self.setCentralWidget(form)

    def _registerBook(self):
        Book(self.titleInput.text(),self.authorInput.text(),int(self.isbnInput.text()),self.genreInput.text(),float(self.weightInput.text()),float(self.valueInput.text()))
        QMessageBox.information(self, "Success", "Book has been successfully added.")

    def searchBook(self):
        """Displays a search panel for books."""
        
        self.bookSearchWidget = QWidget()
        mainLayout = QVBoxLayout()

        # Combo criterio
        self.bookCriteriaCombo = QComboBox()
        self.bookCriteriaCombo.addItems(["Title", "Author", "ISBN"])

        # Input búsqueda
        self.bookSearchInput = QLineEdit()

        # Layout del formulario
        formLayout = QFormLayout()
        formLayout.addRow("Search by:", self.bookCriteriaCombo)
        formLayout.addRow("Value:", self.bookSearchInput)

        # Botón actualizar
        updateBtn = QPushButton("Update Search")
        updateBtn.clicked.connect(self._updateBookSearch)

        # ListWidget para mostrar resultados
        self.bookListWidget = QListWidget()

        # Añadir todo al layout principal
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(updateBtn)
        mainLayout.addWidget(self.bookListWidget)

        self.bookSearchWidget.setLayout(mainLayout)
        self.setCentralWidget(self.bookSearchWidget)

        # Ejecutar búsqueda inicial
        self._updateBookSearch()

    def _updateBookSearch(self):
        """Updates search results based on current criterion and input."""
        criterion = self.bookCriteriaCombo.currentText()
        value = self.bookSearchInput.text()

        self.bookListWidget.clear()

        if criterion == 'Title':
            results = BookManager.lookUpByTitle(value)
        elif criterion == 'Author':
            results = BookManager.lookUpByAuthor(value)
        elif criterion == 'ISBN':
            results = [BookManager.lookUpByISBN(int(value))]
            if not results:
                results = []

        # Fill ListWidget
        for book in results:
            self.bookListWidget.addItem(str(book))

        if not results:
            self.bookListWidget.addItem("No results found.")

    def deleteBook(self):
        """Creates a pop-up window to delete a book by ISBN."""

        # --- Create the new small window ---
        self.deleteWindow = QWidget()
        self.deleteWindow.setWindowTitle("Delete Book")
        self.deleteWindow.setFixedSize(300, 150)

        layout = QVBoxLayout(self.deleteWindow)

        # Label
        label = QLabel("Enter ISBN of the book to delete:")
        layout.addWidget(label)

        # Input field
        self.deleteIsbnInput = QLineEdit()
        self.deleteIsbnInput.setPlaceholderText("ISBN")
        layout.addWidget(self.deleteIsbnInput)

        # Delete button
        deleteButton = QPushButton("Delete")
        layout.addWidget(deleteButton)

        # Connect button to the internal delete logic
        deleteButton.clicked.connect(self._confirmDeleteBook)

        # Show the window
        self.deleteWindow.show()

    def _confirmDeleteBook(self):
        """Handles deletion once user presses the delete button in the pop-up."""

        isbn_text = self.deleteIsbnInput.text().strip()

        # Validate numeric ISBN
        if not isbn_text.isdigit():
            QMessageBox.warning(self.deleteWindow, "Invalid Input",
                                "Please enter a valid numeric ISBN.")
            return

        isbn = int(isbn_text)

        # Look up the book
        book = BookManager.lookUpByISBN(isbn)

        if book is None:
            QMessageBox.information(
                self.deleteWindow,
                "Book Not Found",
                f"No book exists with ISBN {isbn}."
            )
            return

        # Delete the book
        BookManager.removeBook(book)

        QMessageBox.information(
            self.deleteWindow,
            "Book Deleted",
            f"The book with ISBN {isbn} was successfully deleted."
        )

        # Close the delete window
        self.deleteWindow.close()