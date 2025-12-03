from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
from managers.bookManager import BookManager
from managers.lendingManager import LendingManager
from managers.userManager import UserManager

class LendingMenuActions:
    def lendBook(self):
        """Creates a pop-up window to lend a book to a user."""

        self.lendWindow = QWidget()
        self.lendWindow.setWindowTitle("Lend Book")
        self.lendWindow.setFixedSize(320, 200)

        layout = QVBoxLayout(self.lendWindow)

        # User ID input
        layout.addWidget(QLabel("Enter User ID:"))
        self.lendUserInput = QLineEdit()
        self.lendUserInput.setPlaceholderText("User ID")
        layout.addWidget(self.lendUserInput)

        # Book ISBN input
        layout.addWidget(QLabel("Enter Book ISBN:"))
        self.lendIsbnInput = QLineEdit()
        self.lendIsbnInput.setPlaceholderText("ISBN")
        layout.addWidget(self.lendIsbnInput)

        # Lend button
        lendBtn = QPushButton("Lend Book")
        lendBtn.clicked.connect(self._confirmLendBook)
        layout.addWidget(lendBtn)

        self.lendWindow.show()


    def _confirmLendBook(self):
        """Validates inputs and lends the book."""

        user_id_txt = self.lendUserInput.text().strip()
        isbn_txt = self.lendIsbnInput.text().strip()

        # Validate ID
        if not user_id_txt.isdigit():
            QMessageBox.warning(self.lendWindow, "Invalid Input", "User ID must be numeric.")
            return

        # Validate ISBN
        if not isbn_txt.isdigit():
            QMessageBox.warning(self.lendWindow, "Invalid Input", "ISBN must be numeric.")
            return

        user_id = int(user_id_txt)
        isbn = int(isbn_txt)

        # Lookup user
        user = UserManager.lookUpByID(user_id)
        if user is None:
            QMessageBox.information(
                self.lendWindow, "User Not Found", f"No user found with ID {user_id}."
            )
            return

        # Lookup book
        book = BookManager.lookUpByISBN(isbn)
        if book is None:
            QMessageBox.information(
                self.lendWindow, "Book Not Found", f"No book found with ISBN {isbn}."
            )
            return

        # Check availability
        if BookManager.stock[str(book)] <= 0:
            QMessageBox.information(
                self.lendWindow,
                "Unavailable",
                f"'{book.title}' is not available right now."
            )
            return

        # Process lending
        LendingManager.lendBook(user, book)

        QMessageBox.information(
            self.lendWindow,
            "Success",
            f"The book '{book.title}' was lent to user {user_id}."
        )

        self.lendWindow.close()

    def returnBook(self):
        """Creates a pop-up window to return a book by ISBN."""

        self.returnWindow = QWidget()
        self.returnWindow.setWindowTitle("Return Book")
        self.returnWindow.setFixedSize(300, 160)

        layout = QVBoxLayout(self.returnWindow)

        layout.addWidget(QLabel("Enter Book ISBN to return:"))

        self.returnIsbnInput = QLineEdit()
        self.returnIsbnInput.setPlaceholderText("ISBN")
        layout.addWidget(self.returnIsbnInput)

        returnBtn = QPushButton("Return Book")
        returnBtn.clicked.connect(self._confirmReturnBook)
        layout.addWidget(returnBtn)

        self.returnWindow.show()


    def _confirmReturnBook(self):
        """Validates ISBN input and processes the return."""

        isbn_txt = self.returnIsbnInput.text().strip()

        if not isbn_txt.isdigit():
            QMessageBox.warning(self.returnWindow, "Invalid Input", "ISBN must be numeric.")
            return

        isbn = int(isbn_txt)

        # Lookup book
        book = BookManager.lookUpByISBN(isbn)
        if book is None:
            QMessageBox.information(
                self.returnWindow, "Book Not Found", f"No book with ISBN {isbn}."
            )
            return

        # Process return
        LendingManager.returnBook(book)

        QMessageBox.information(
            self.returnWindow,
            "Book Returned",
            f"'{book.title}' has been successfully returned."
        )

        self.returnWindow.close()