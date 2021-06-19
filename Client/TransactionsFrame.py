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
from Client.GetMessageFrame import GetMessageFrame
from Client.SetMessageFrame import SetMessageFrame


class TransactionsFrame(TitleFrame):
    def __init__(self,
                 layout_direction: LayoutDirection,
                 contract_connection: HistoryCoinContract):
        super().__init__("Transactions",
                         layout_direction)
        self.frame = Frame(LayoutDirection.HORIZONTAL)
        self.add_widget(self.frame)
        self.get_message_frame = GetMessageFrame(LayoutDirection.VERTICAL,
                                                 contract_connection)
        self.frame.add_widget(self.get_message_frame)

        self.set_message_frame = SetMessageFrame(LayoutDirection.VERTICAL,
                                                 contract_connection)
        self.frame.add_widget(self.set_message_frame)
        self.frame.add_spacer(SpacerDirection.HORIZONTAL)
        self.add_spacer(SpacerDirection.VERTICAL)


