from PyQt6.QtWidgets import (
    QMainWindow, QMenuBar, QMenu, QWidget
)

# Import menu action classes
from .bookMenu import BookMenuActions
from .userMenu import UserMenuActions
from .lendingMenu import LendingMenuActions
from .bookshelfMenu import BookshelfMenuActions
from .statisticsMenu import StatisticsMenuActions

class LibraryGUI(
    QMainWindow,
    BookMenuActions,
    UserMenuActions,
    LendingMenuActions,
    BookshelfMenuActions,
    StatisticsMenuActions
):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Management System")
        self.setGeometry(200, 200, 600, 400)

        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self._createMenu()

    def _createMenu(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        # BOOK MENU
        bookMenu = QMenu("Books", self)
        menuBar.addMenu(bookMenu)

        bookMenu.addAction("Add Book", self.addBook)
        bookMenu.addAction("Search Book", self.searchBook)
        bookMenu.addAction("Delete Book", self.deleteBook)

        # USER MENU
        userMenu = QMenu("Users", self)
        menuBar.addMenu(userMenu)

        userMenu.addAction("Add User", self.addUser)
        userMenu.addAction("Search Users", self.searchUser)
        userMenu.addAction("Delete User", self.deleteUser)

        # LENDING MENU
        lendingMenu = QMenu("Lending", self)
        menuBar.addMenu(lendingMenu)

        lendingMenu.addAction("Lend Book", self.lendBook)
        lendingMenu.addAction("Return Book", self.returnBook)

        # BOOKSHELF MENU
        bookshelfMenu = QMenu("Bookshelf", self)
        menuBar.addMenu(bookshelfMenu)

        bookshelfMenu.addAction("Worst combinations", self.getWorstCombination)
        bookshelfMenu.addAction("Optimal combination", self.getOptimalCombination)

        # STATISTICS MENU
        statisticsMenu = QMenu("Statistics", self)
        menuBar.addMenu(statisticsMenu)

        statisticsMenu.addAction("Inventory statistics", self.getInventoryStatistics)
        statisticsMenu.addAction("Author statistics", self.getAuthorStatistics)