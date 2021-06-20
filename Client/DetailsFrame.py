import sys
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPlainTextEdit,
                             QLineEdit,
                             QLabel,
                             QFrame)
from PyQt6.QtGui import QFont, QAction, QIcon
from Client.TitleFrame import TitleFrame
from HistoryCoinContract import HistoryCoinContract
from Client.Frame import LayoutDirection, SpacerDirection


class DetailsFrame(TitleFrame):
    def __init__(self):
        super().__init__("Transaction Details",
                         LayoutDirection.VERTICAL)
        self.setFixedHeight(300)
        self.layout.addWidget(QLabel("Output"))
        self.output_text_box = QPlainTextEdit()
        self.layout.addWidget(self.output_text_box)
        self.layout.addWidget(QLabel("Details"))
        self.details_text_box = QPlainTextEdit()
        self.layout.addWidget(self.details_text_box)
        # self.add_spacer(SpacerDirection.VERTICAL)

    def log_output(self, text: str):
        self.output_text_box.setPlainText(text)

    def log_details(self, text: str):
        self.details_text_box.setPlainText(text)

