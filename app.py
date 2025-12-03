import sys
from ui import LibraryGUI
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
window = LibraryGUI()
window.show()
sys.exit(app.exec())