import sys
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QVBoxLayout,
                             QFrame)
from PyQt6.QtGui import QFont, QAction, QIcon
from Client.Frame import Frame, LayoutDirection
from HistoryCoinContract import HistoryCoinContract
from Client.DetailsFrame import DetailsFrame
from Client.TransactionsFrame import TransactionsFrame


class MainWindow(QMainWindow):  # form
    def __init__(self):
        super().__init__(None)
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)
        self.setWindowTitle("History Coin Client")
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(1000, 800)
        self.frame = Frame(LayoutDirection.GRID)
        self.setCentralWidget(self.frame)
        self.build_menu()
        self.center()
        self.show()
        self.contract_connection = HistoryCoinContract()
        self.details_frame = DetailsFrame()
        self.frame.layout.addWidget(self.details_frame, 1, 0)
        self.transactions_frame = TransactionsFrame(LayoutDirection.GRID, self.contract_connection, self.details_frame)
        self.frame.layout.addWidget(self.transactions_frame, 0, 0)

    def notify_details(self, text: str):
        self.details_frame.log_output(text)

    def center(self):
        rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

    def build_menu(self):
        deploy_menu_action = QAction('Deploy Contract', self)
        deploy_menu_action.triggered.connect(self.deploy_contract)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(deploy_menu_action)

    def deploy_contract(self):
        print("deploying contract")