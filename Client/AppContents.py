import sys
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QFrame)
from PyQt6.QtGui import QFont, QAction, QIcon
from Client.Frame import Frame
from Contract import HistoryCoinContract
from Client.Frame import LayoutDirection, SpacerDirection


class AppContents(Frame):
    def __init__(self, contract_connection: HistoryCoinContract):
        super().__init__(LayoutDirection.VERTICAL)
        self.contract_connection = contract_connection
        self.display_message_label = QLabel()
        self.add_widget(self.display_message_label)
        self.get_message_button = QPushButton("get message")
        self.get_message_button.clicked.connect(self.get_message)
        self.add_widget(self.get_message_button)
        self.set_message_line_edit = QLineEdit()
        self.add_widget(self.set_message_line_edit)
        self.set_message_button = QPushButton("set message")
        self.set_message_button.clicked.connect(self.set_message)
        self.add_widget(self.set_message_button)
        self.add_spacer(SpacerDirection.VERTICAL)

    def get_message(self):
        self.display_message_label.setText(self.contract_connection.get_message())

    def set_message(self):
        self.contract_connection.set_message(self.set_message_line_edit.text())
        self.get_message()
