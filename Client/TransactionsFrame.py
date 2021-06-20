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
from Client.TitleFrame import TitleFrame
from Client.GetMessageFrame import GetMessageFrame
from Client.SetMessageFrame import SetMessageFrame
from Client.MakeProposalFrame import MakeProposalFrame
from Client.DetailsFrame import DetailsFrame


class TransactionsFrame(TitleFrame):
    def __init__(self,
                 layout_direction: LayoutDirection,
                 contract_connection: HistoryCoinContract,
                 details_frame: DetailsFrame):
        super().__init__("Transactions",
                         layout_direction)
        self.frame = Frame(LayoutDirection.GRID)
        self.layout.addWidget(self.frame)

        self.get_message_frame = GetMessageFrame(LayoutDirection.VERTICAL, contract_connection, details_frame)
        self.frame.layout.addWidget(self.get_message_frame, 0, 0)

        self.set_message_frame = SetMessageFrame(LayoutDirection.VERTICAL, contract_connection, details_frame)
        self.frame.layout.addWidget(self.set_message_frame, 0, 1)

        self.make_proposal_frame = MakeProposalFrame(LayoutDirection.VERTICAL, contract_connection, details_frame)
        self.frame.layout.addWidget(self.make_proposal_frame, 0, 2)

        self.frame.add_spacer(SpacerDirection.HORIZONTAL)
        self.add_spacer(SpacerDirection.VERTICAL)


