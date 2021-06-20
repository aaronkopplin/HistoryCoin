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


class MakeProposalFrame(TitleFrame):
    def __init__(self,
                 layout_direction: LayoutDirection,
                 contract_connection: HistoryCoinContract,
                 details_frame: DetailsFrame):
        super().__init__("Make Proposal",
                         layout_direction)
        self.details_frame = details_frame
        self.contract_connection = contract_connection
        self.param_one = QLineEdit()
        self.layout.addWidget(self.param_one)
        self.param_two = QLineEdit()
        self.layout.addWidget(self.param_two)
        self.add_spacer(SpacerDirection.VERTICAL)
        self.call_function_button = QPushButton("propose record")
        self.call_function_button.clicked.connect(self.call_function)
        self.layout.addWidget(self.call_function_button)

    def call_function(self):
        output = self.contract_connection.make_proposal(self.param_one.text(), int(self.param_two.text()))
        print(output)
        self.details_frame.log_output(str(output))










