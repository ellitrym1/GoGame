from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtWidgets import QFrame, QPushButton, QGridLayout, QLabel
from game import game
from stone import stone

class board(QFrame):
    updateCaptureSignal = pyqtSignal(str, int)
    updateTerritorySignal = pyqtSignal(str, int)
    def __init__(self):
        super().__init__()
        self.setFixedSize(510, 500)
        self.setMinimumWidth(500)
        self.setStyleSheet("background-color: rgb(79, 79, 79)")
        self.boardWidth = 7
        self.boardHeight = 7
        self.boardArr = [[stone(0, r, c) for r in range(0, self.boardWidth)] for c in range(0, self.boardHeight)]
        self.game = game()


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawBoardGrid(painter)
        self.drawStones(painter)

    def drawBoardGrid(self, painter):
        brush = QBrush(Qt.SolidPattern)
        self.white = QColor(212, 154, 44)
        self.black = QColor(51, 16, 8)
        brush.setColor(self.black)
        painter.setBrush(brush)
        for r in range(0, self.boardHeight):
            for c in range(0, self.boardWidth):
                painter.save()
                colTransformation = self.squareWidth() * c
                rowTransformation = self.squareHeight() * r
                painter.translate(colTransformation, rowTransformation)
                painter.fillRect(c, r, self.squareWidth(), self.squareHeight(), brush)
                painter.restore()
                if brush.color() == self.white:
                    brush.setColor(self.black)
                else:
                    brush.setColor(self.white)

    def drawStones(self, painter):
        color = Qt.transparent
        for r in range(0, self.boardWidth):
            for c in range(0, self.boardHeight):
                painter.save()
                painter.translate((self.squareWidth() * r) + self.squareWidth() / 2,
                                  (self.squareHeight() * c) + self.squareHeight() / 2)

                if self.boardArr[c][r].getStoneColor() == 0:
                    color = QColor(Qt.transparent)
                elif self.boardArr[c][r].getStoneColor() == 1:
                    color = QColor(0, 0, 0)
                elif self.boardArr[c][r].getStoneColor() == 2:
                    color = QColor(255, 255, 255)

                painter.setBrush(color)

                radius = (self.squareWidth() - 2) / 2
                center = QPoint(radius, radius)
                painter.drawEllipse(center, radius, radius)
                painter.restore()

    def tryToPlaceStone(self):
        if self.game.vacant():
            if self.game.suicideRule():
                return False
            else:
                return True

    def placeStone(self):
        self.game.placeStone()
        self.game.updateLiberties()
        if self.game.updateStonesCaptured() != None:
            print("Captured")
            self.game.updateLiberties()

        self.game.updateTerritories()
        self.game.removeStone()
        print(self.game.blackStonesCaptured)
        print(self.game.whiteStonesCaptured)
        print(self.game.blackTerritories)
        print(self.game.whiteTerritories)


    def squareWidth(self):
        return self.contentsRect().width() / self.boardWidth

    def squareHeight(self):
        return self.contentsRect().height() / self.boardHeight

    def passTurn(self):
        self.game.changeTurn()

    def resetGame(self):
        self.boardArr = [[stone(0, r, c) for r in range(self.boardWidth)] for c in range(self.boardHeight)]
        self.game.turn = 1
        self.game.blackTerritories = 0
        self.game.blackStonesCaptured = 0
        self.game.whiteTerritories = 0
        self.game.whiteStonesCaptured = 0
        self.printBoardConsole()

    def getWhiteStonesCaptured(self):
        return self.game.whiteStonesCaptured

    def getBlackStonesCaptured(self):
        return self.game.blackStonesCaptured

    def getWhiteTerritories(self):
        return self.game.whiteTerritories

    def getBlackTerritories(self):
        return self.game.blackTerritories

    def getCurrentPlayer(self):
        return self.game.getTurn()

    def printBoardConsole(self):
        for r in self.boardArr:
            for c in r:
               if c.getStoneColor() == 0:
                   print(" 0 ", end=" ")
               if c.getStoneColor() == 1:
                   print(" 1 ", end=" ")
               if c.getStoneColor() == 2:
                   print(" 2 ", end=" ")
            print('\n')

    def updateCaptureAndTerritory(self):
        self.updateCaptureSignal.emit(str(self.game.getWhiteStonesCaptured()), 2)
        self.updateCaptureSignal.emit(str(self.game.getBlackStonesCaptured()), 1)
        self.updateTerritorySignal.emit(str(self.game.getWhiteStonesCaptured()), 2)
        self.updateTerritorySignal.emit(str(self.game.getBlackStonesCaptured()), 1)

    def mousePressEvent(self, event):
        x = event.x()
        xc = round(x / self.squareWidth()) - 1
        y = event.y()
        yc = round(y / self.squareHeight()) - 1
        self.game.updateVars(xc, yc, self.boardArr)
        if self.tryToPlaceStone():
            self.placeStone()
            self.updateCaptureAndTerritory()

        self.printBoardConsole()
        self.update()



