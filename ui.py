from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QMenuBar, QMenu
)

class LibraryGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Management System")
        self.setGeometry(200, 200, 600, 400)

        self._createMenu()
        self._createButtons()

    def _createMenu(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        # BOOK MENU
        bookMenu = QMenu("Books", self)
        menuBar.addMenu(bookMenu)

        addBookAction = bookMenu.addAction("Add Book")
        addBookAction.triggered.connect(self.addBook)

        removeBookAction = bookMenu.addAction("Remove Book")
        removeBookAction.triggered.connect(self.removeBook)

        listBooksAction = bookMenu.addAction("List Books")
        listBooksAction.triggered.connect(self.listBooks)

        # USER MENU
        userMenu = QMenu("Users", self)
        menuBar.addMenu(userMenu)

        addUserAction = userMenu.addAction("Add User")
        addUserAction.triggered.connect(self.addUser)

        removeUserAction = userMenu.addAction("Remove User")
        removeUserAction.triggered.connect(self.removeUser)

        listUsersAction = userMenu.addAction("List Users")
        listUsersAction.triggered.connect(self.listUsers)

        # LENDING MENU
        lendingMenu = QMenu("Lending", self)
        menuBar.addMenu(lendingMenu)

        lendBookAction = lendingMenu.addAction("Lend Book")
        lendBookAction.triggered.connect(self.lendBook)

        returnBookAction = lendingMenu.addAction("Return Book")
        returnBookAction.triggered.connect(self.returnBook)

        historyAction = lendingMenu.addAction("View Lending History")
        historyAction.triggered.connect(self.viewHistory)

    def _createButtons(self):
        container = QWidget()
        layout = QVBoxLayout()

        # MAIN ACTION BUTTONS
        btnAddBook = QPushButton("Add Book")
        btnAddBook.clicked.connect(self.addBook)

        btnLendBook = QPushButton("Lend Book")
        btnLendBook.clicked.connect(self.lendBook)

        btnReturnBook = QPushButton("Return Book")
        btnReturnBook.clicked.connect(self.returnBook)

        btnListBooks = QPushButton("List All Books")
        btnListBooks.clicked.connect(self.listBooks)

        layout.addWidget(btnAddBook)
        layout.addWidget(btnLendBook)
        layout.addWidget(btnReturnBook)
        layout.addWidget(btnListBooks)

        container.setLayout(layout)
        self.setCentralWidget(container)

    # ---------------------------
    # ACTION METHODS (empty)
    # ---------------------------

    def addBook(self):
        # This action should open a dialog to add a new book to the collection.
        pass

    def removeBook(self):
        # This action should remove a selected book from the system.
        pass

    def listBooks(self):
        # This action should display a list of all books stored in the system.
        pass

    def addUser(self):
        # This action should open a dialog to register a new user in the system.
        pass

    def removeUser(self):
        # This action should remove a selected user from the registry.
        pass

    def listUsers(self):
        # This action should display all registered users.
        pass

    def lendBook(self):
        # This action should create a new lending record and reduce book availability.
        pass

    def returnBook(self):
        # This action should process the return of a book and update its availability.
        pass

    def viewHistory(self):
        # This action should show users' lending history or transactions performed.
        pass