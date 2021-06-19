import sys
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QVBoxLayout,
                             QFrame)
from PyQt6.QtGui import QFont, QAction, QIcon
from Client.Frame import Frame
from Contract import HistoryCoinContract
from Client.AppContents import AppContents


class MainWindow(QMainWindow):  # form
    def __init__(self):
        super().__init__(None)
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)
        self.setWindowTitle("History Coin Client")
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(1000, 800)
        self.frame = Frame()  # self.frame.setStyleSheet("background-color: rgb(100, 200, 100); ")
        self.setCentralWidget(self.frame)
        self.build_menu()
        self.center()
        self.show()
        self.history_coin_contract = HistoryCoinContract()
        self.app_contents = AppContents(self.history_coin_contract)
        self.frame.add_widget(self.app_contents)

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