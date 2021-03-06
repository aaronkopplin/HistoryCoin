import sys
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QFrame)
from PyQt6.QtGui import QFont, QAction, QIcon
from Client.Frame import Frame
from HistoryCoinContract import HistoryCoinContract
from Client.Frame import LayoutDirection, SpacerDirection
from Client.DetailsFrame import DetailsFrame
from Client.TitleFrame import TitleFrame


class GetMessageFrame(TitleFrame):
    def __init__(self,
                 layout_direction: LayoutDirection,
                 contract_connection: HistoryCoinContract,
                 details_frame: DetailsFrame):
        super().__init__("Get Message",
                         layout_direction)
        self.details_frame = details_frame
        self.contract_connection = contract_connection
        self.display_message_label = QLabel()
        self.layout.addWidget(self.display_message_label)
        self.add_spacer(SpacerDirection.VERTICAL)
        self.get_message_button = QPushButton("get message")
        self.get_message_button.clicked.connect(self.get_message)
        self.layout.addWidget(self.get_message_button)

    def get_message(self):
        self.display_message_label.setText(self.contract_connection.get_message())
