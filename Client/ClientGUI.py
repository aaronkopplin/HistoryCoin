import sys
from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QPushButton,
                             QApplication,
                             QVBoxLayout,
                             QFrame)
from PyQt6.QtGui import QFont, QAction, QIcon
from Client.Frame import Frame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.setMinimumWidth(1100)
        self.setMinimumHeight(600)
        self.setWindowTitle("History Coin Client")
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(1000, 800)

        self.frame = Frame()
        self.setCentralWidget(self.frame)
        self.frame.add_widget(QPushButton("button"))
        self.frame.add_widget(QPushButton("button"))
        self.center()
        self.build_menu()

        self.show()

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