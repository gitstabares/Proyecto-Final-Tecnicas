import sys
from ui.main import LibraryGUI
from PyQt6.QtWidgets import QApplication
from utils.repository import *

loadData()
app = QApplication(sys.argv)
window = LibraryGUI()
window.show()
sys.exit(app.exec())