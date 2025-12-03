from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
)
from managers.bookshelf import Bookshelf

class BookshelfMenuActions:
    def getWorstCombination(self):
        """Displays the worst bookshelf combinations using Bookshelf.poorBookshelf()."""

        # Create window
        self.worstWin = QWidget()
        self.worstWin.setWindowTitle("Worst Book Combinations")
        self.worstWin.setFixedSize(420, 350)

        layout = QVBoxLayout(self.worstWin)

        layout.addWidget(QLabel("Worst Book Combinations (Poor Bookshelf):"))

        # List widget
        self.worstListWidget = QListWidget()
        layout.addWidget(self.worstListWidget)

        # Get data
        combinations = Bookshelf.poorBookshelf()

        # Populate list
        for combo in combinations:
            text = ", ".join([book.title for book in combo])
            item = QListWidgetItem(text)
            self.worstListWidget.addItem(item)

        if not combinations:
            self.worstListWidget.addItem("No combinations found.")

        self.worstWin.show()

    def getOptimalCombination(self):
        """Displays the optimal bookshelf combination with its total price."""

        # Create window
        self.optimalWin = QWidget()
        self.optimalWin.setWindowTitle("Optimal Book Combination")
        self.optimalWin.setFixedSize(420, 380)

        layout = QVBoxLayout(self.optimalWin)

        layout.addWidget(QLabel("Optimal Book Combination:"))

        # List widget for the books
        self.optimalListWidget = QListWidget()
        layout.addWidget(self.optimalListWidget)

        # Label for total value
        self.totalValueLabel = QLabel()
        layout.addWidget(self.totalValueLabel)

        # Get data
        bestValue, bestCombo = Bookshelf.optimalBookshelf()

        for book in bestCombo:
            self.optimalListWidget.addItem(str(book))

        # Show price
        self.totalValueLabel.setText(f"Total Value: ${bestValue}")

        if not bestCombo:
            self.optimalListWidget.addItem("No optimal combination found.")

        self.optimalWin.show()