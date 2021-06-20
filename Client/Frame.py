from enum import Enum
from PyQt6.QtWidgets import (QWidget,
                             QGridLayout,
                             QSpacerItem,
                             QSizePolicy,
                             QVBoxLayout,
                             QHBoxLayout,
                             QFrame)


class SpacerDirection(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class LayoutDirection(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    GRID = "GRID"


class Frame(QFrame):
    def __init__(self,
                 layout=LayoutDirection):
        super().__init__()
        if layout == LayoutDirection.VERTICAL:
            self.layout = QVBoxLayout()
        elif layout == LayoutDirection.HORIZONTAL:
            self.layout = QHBoxLayout()
        elif layout == LayoutDirection.GRID:
            self.layout = QGridLayout()

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def add_item(self, widget: QSpacerItem):
        self.layout.addItem(widget)

    def add_spacer(self, spacer_direction: SpacerDirection):
        if spacer_direction.value == SpacerDirection.VERTICAL.value:
            self.add_item(QSpacerItem(10, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding))
        else:
            self.add_item(QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))
