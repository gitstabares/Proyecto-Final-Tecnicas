from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QListWidget,
    QLineEdit, QPushButton, QMessageBox
)
from managers.bookManager import BookManager

class StatisticsMenuActions:
    def getInventoryStatistics(self):
        """Displays inventory statistics using BookManager.generateReport()."""

        # Create the window
        self.invWin = QWidget()
        self.invWin.setWindowTitle("Inventory Statistics")
        self.invWin.setFixedSize(450, 350)

        layout = QVBoxLayout(self.invWin)

        layout.addWidget(QLabel("Inventory Report:"))

        # List widget
        self.inventoryListWidget = QListWidget()
        layout.addWidget(self.inventoryListWidget)

        # Get report
        report = BookManager.generateReport()  # expected list

        if report:
            for line in report:
                self.inventoryListWidget.addItem(str(line))
        else:
            self.inventoryListWidget.addItem("No inventory information available.")

        self.invWin.show()

    def getAuthorStatistics(self):
        """Creates a window to query statistics of an author's books."""

        # Create window
        self.authWin = QWidget()
        self.authWin.setWindowTitle("Author Statistics")
        self.authWin.setFixedSize(420, 260)

        layout = QVBoxLayout(self.authWin)

        # Input label + field
        layout.addWidget(QLabel("Enter Author Name:"))
        self.authorInput = QLineEdit()
        layout.addWidget(self.authorInput)

        # Button
        self.generateAuthorBtn = QPushButton("Generate")
        layout.addWidget(self.generateAuthorBtn)

        # Output labels
        self.totalValueLabel = QLabel("Total Value: ")
        self.avgWeightLabel = QLabel("Average Weight: ")

        layout.addWidget(self.totalValueLabel)
        layout.addWidget(self.avgWeightLabel)

        # Connect
        self.generateAuthorBtn.clicked.connect(self._generateAuthorStats)

        self.authWin.show()


    def _generateAuthorStats(self):
        """Generates and displays stats for the requested author."""

        author = self.authorInput.text().strip()

        if not author:
            QMessageBox.warning(self, "Invalid Input", "Please enter an author name.")
            return

        # Get data
        total = BookManager.totalPrice(author)
        avg = BookManager.meanWeight(author)

        # If no books found, probably return 0
        if total == 0 and avg == 0:
            QMessageBox.information(
                self, 
                "No Books Found", 
                f"No books found for author '{author}'."
            )
            return

        # Show results
        self.totalValueLabel.setText(f"Total Value: {total}")
        self.avgWeightLabel.setText(f"Average Weight: {avg}")