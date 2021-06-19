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
from Client.TransactionsFrame import TransactionsFrame


class AppContents(Frame):
    def __init__(self,
                 layout_direction: LayoutDirection,
                 contract_connection: HistoryCoinContract):
        super().__init__(layout_direction)
        self.transactions_frame = TransactionsFrame(LayoutDirection.VERTICAL, contract_connection)
        self.add_widget(self.transactions_frame)
        self.details_frame = DetailsFrame()
        self.add_widget(self.details_frame)

