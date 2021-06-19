from enum import Enum
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QSpacerItem,
                             QSizePolicy,
                             QVBoxLayout,
                             QHBoxLayout,
                             QFrame)


class SpacerDirection(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


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

    def add_item(self, widget: QSpacerItem):
        self.layout.addItem(widget)

    def add_spacer(self, spacer_direction: SpacerDirection):
        if spacer_direction.value == SpacerDirection.VERTICAL.value:
            # QSpacerItem()
            self.add_item(QSpacerItem(10, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding))
        else:
            self.add_item(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))
