import sys
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QFrame)
from PyQt6.QtGui import QFont, QAction, QIcon
from Client.TitleFrame import TitleFrame
from Contract import HistoryCoinContract
from Client.Frame import LayoutDirection, SpacerDirection


class DetailsFrame(TitleFrame):
    def __init__(self):
        super().__init__("Transaction Details",
                         LayoutDirection.VERTICAL)
        self.setFixedHeight(100)
        self.add_spacer(SpacerDirection.VERTICAL)