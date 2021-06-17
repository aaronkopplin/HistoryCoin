import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication)
from Client.ClientGUI import MainWindow


def main():
    app = QApplication([])
    client = MainWindow()
    client.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
