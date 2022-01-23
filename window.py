import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QAction, QApplication

from gameArea import gameArea
from sideBar import sideBar

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" Go Game")
        self.setWindowIcon(QIcon("./icons/chess-board.png"))
        top = 100
        left = 100
        width = 800
        height = 600
        self.setFixedSize(width, height)

        self.grid = QGridLayout()

        self.sideBar = sideBar()
        self.gameArea = gameArea()

        self.grid.addWidget(self.gameArea, 0, 0, 4, 3)
        self.grid.addWidget(self.sideBar, 0, 2, 4, 1)

        win = QWidget()
        win.setLayout(self.grid)
        self.setCentralWidget(win)

        menu = self.menuBar()

        gameMenu = menu.addMenu("Game")
        helpMenu = menu.addMenu("Help")

        newAction = QAction("New", self)
        newAction.setShortcut("Ctrl+N")
        gameMenu.addAction(newAction)
        newAction.triggered.connect(self.newGame)

        resetAction = QAction("Reset", self)
        resetAction.setShortcut("Ctrl+R")
        gameMenu.addAction(resetAction)
        resetAction.triggered.connect(self.resetGame)

        membersAction = QAction("Members", self)
        helpMenu.addAction(membersAction)
        membersAction.triggered.connect(self.members)

        rulesAction = QAction("Rules", self)
        helpMenu.addAction(rulesAction)
        rulesAction.triggered.connect(self.rules)

        aboutAction = QAction("About", self)
        helpMenu.addAction(aboutAction)
        aboutAction.triggered.connect(self.about)

    def newGame(self):
        print("New Game")

    def resetGame(self):
        print("Reset Game")

    def members(self):
        print("Members")

    def rules(self):
        print("Rules")

    def about(self):
        print("About")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec()


