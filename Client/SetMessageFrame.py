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
from Client.DetailsFrame import DetailsFrame
from Client.TitleFrame import TitleFrame


class SetMessageFrame(TitleFrame):
    def __init__(self,
                 layout_direction: LayoutDirection,
                 contract_connection: HistoryCoinContract):
        super().__init__("Get Message",
                         layout_direction)
        self.setFixedWidth(400)
        self.contract_connection = contract_connection
        self.set_message_line_edit = QLineEdit()
        self.add_widget(self.set_message_line_edit)
        self.set_message_button = QPushButton("set message")
        self.set_message_button.clicked.connect(self.set_message)
        self.add_widget(self.set_message_button)

    def set_message(self):
        self.contract_connection.set_message(self.set_message_line_edit.text())
