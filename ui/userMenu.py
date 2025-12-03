from PyQt6.QtWidgets import (
    QWidget, QFormLayout, QLineEdit,
    QPushButton, QMessageBox, QVBoxLayout,
    QComboBox, QListWidget, QLabel
)
from models.user import User
from managers.userManager import UserManager

class UserMenuActions:

    def addUser(self):
        """Displays a form to register a new user."""

        form = QWidget()
        layout = QFormLayout()

        self.userNameInput = QLineEdit()
        self.userIdInput = QLineEdit()

        layout.addRow("Name:", self.userNameInput)
        layout.addRow("User ID:", self.userIdInput)

        registerBtn = QPushButton("Register User")
        registerBtn.clicked.connect(self._registerUser)

        layout.addRow(registerBtn)

        form.setLayout(layout)
        self.setCentralWidget(form)

    def _registerUser(self):
        User(self.userNameInput.text(),int(self.userIdInput.text()))
        QMessageBox.information(self, "Success", "User has been successfully registered.")

    def searchUser(self):
        """Displays a search panel for users"""
        
        self.userSearchWidget = QWidget()
        mainLayout = QVBoxLayout()

        # Combo criterio
        self.searchCriteriaCombo = QComboBox()
        self.searchCriteriaCombo.addItems(["Name","ID"])

        # Input búsqueda
        self.userSearchInput = QLineEdit()

        # Layout del formulario
        formLayout = QFormLayout()
        formLayout.addRow("Search by:", self.searchCriteriaCombo)
        formLayout.addRow("Value:", self.userSearchInput)

        # Botón actualizar
        updateBtn = QPushButton("Update Search")
        updateBtn.clicked.connect(self._updateUserSearch)

        # ListWidget para mostrar resultados
        self.userListWidget = QListWidget()

        # Añadir todo al layout principal
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(updateBtn)
        mainLayout.addWidget(self.userListWidget)

        self.userSearchWidget.setLayout(mainLayout)
        self.setCentralWidget(self.userSearchWidget)

        # Ejecutar búsqueda inicial
        self._updateUserSearch()


    def _updateUserSearch(self):
        """Updates search results based on current criterion and input."""
        criterion = self.searchCriteriaCombo.currentText()
        value = self.userSearchInput.text()

        self.userListWidget.clear()

        if criterion == 'Name':
            results = UserManager.lookUpByName(value)
        elif criterion == 'ID':
            results = [UserManager.lookUpByID(int(value))]
            if not results:
                results = []

        # Fill ListWidget
        for user in results:
            self.userListWidget.addItem(str(user))

        if not results:
            self.userListWidget.addItem("No results found.")

    def deleteUser(self):
        """Creates a pop-up window to delete a user by ID."""

        # Create the user deletion window
        self.deleteUserWindow = QWidget()
        self.deleteUserWindow.setWindowTitle("Delete User")
        self.deleteUserWindow.setFixedSize(300, 150)

        layout = QVBoxLayout(self.deleteUserWindow)

        # Label
        label = QLabel("Enter User ID to delete:")
        layout.addWidget(label)

        # Input field
        self.deleteUserIdInput = QLineEdit()
        self.deleteUserIdInput.setPlaceholderText("User ID")
        layout.addWidget(self.deleteUserIdInput)

        # Delete button
        deleteButton = QPushButton("Delete")
        layout.addWidget(deleteButton)

        # Connect event
        deleteButton.clicked.connect(self._confirmDeleteUser)

        # Show window
        self.deleteUserWindow.show()


    def _confirmDeleteUser(self):
        """Handles deletion once the user presses the delete button."""

        user_id_text = self.deleteUserIdInput.text().strip()

        # Validate numeric or adjust if your ID is alphanumeric
        if not user_id_text.isdigit():
            QMessageBox.warning(
                self.deleteUserWindow,
                "Invalid Input",
                "Please enter a valid numeric User ID."
            )
            return

        user_id = int(user_id_text)

        # Lookup the user
        user = UserManager.lookUpByID(user_id)

        if user is None:
            QMessageBox.information(
                self.deleteUserWindow,
                "User Not Found",
                f"No user exists with ID {user_id}."
            )
            return

        # Delete the user
        UserManager.removeUser(user)

        QMessageBox.information(
            self.deleteUserWindow,
            "User Deleted",
            f"The user with ID {user_id} was successfully deleted."
        )

        # Close pop-up window
        self.deleteUserWindow.close()
