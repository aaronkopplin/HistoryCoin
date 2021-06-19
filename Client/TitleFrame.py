import sys
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QFrame)
from PyQt6.QtGui import QFont, QAction, QIcon
from Client.Frame import Frame, LayoutDirection, SpacerDirection


class TitleFrame(Frame):
    def __init__(self,
                 title: str,
                 layout_direction: LayoutDirection):
        super().__init__(layout_direction)
        self.title = QLabel(title)
        self.title.setStyleSheet("border: 1px solid black;")
        self.add_widget(self.title)
