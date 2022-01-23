from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout

from board import board

class gameArea(QWidget):
    def __init__(self):
        super().__init__()
        self.gamegrid = QVBoxLayout()
        self.board = board()
        self.gamegrid.addWidget(self.board)
        # self.setStyleSheet("padding-left: 0px;"
        #                    "margin-left: 0px;"
        #                    "border: 1px solid black;"
        #                    "")
        self.setLayout(self.gamegrid)

