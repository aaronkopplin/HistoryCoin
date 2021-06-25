from PyQt6.QtWidgets import (QWidget,
                             QMainWindow,
                             QHBoxLayout,
                             QLineEdit,
                             QLabel,
                             QFrame)


class ParameterLineEdit(QFrame):
    def __init__(self, parameter_name: str):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel(parameter_name)
        self.layout.addWidget(self.label)

        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)

    def text(self):
        return self.line_edit.text()