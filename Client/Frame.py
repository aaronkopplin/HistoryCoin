from enum import Enum
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPushButton,
                             QApplication,
                             QVBoxLayout,
                             QHBoxLayout,
                             QFrame)


class LayoutDirection(Enum):
    VERTICAL = QVBoxLayout()
    HORIZONTAL = QHBoxLayout()


class Frame(QFrame):
    def __init__(self,
                 layout=LayoutDirection.VERTICAL):
        super().__init__()
        if layout == LayoutDirection.VERTICAL:
            self.layout = QVBoxLayout()
        else:
            self.layout = QHBoxLayout()

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def add_widget(self, widget: QWidget):
        self.layout.addWidget(widget)
