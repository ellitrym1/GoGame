class stone(object):

    def __init__(self, stoneColor, x, y):
        self.stoneColor = stoneColor
        self.liberties = 0
        self.x = x
        self.y = y

    def getStoneColor(self):
        return self.stoneColor

    def setStoneColor(self, stoneColor):
        print("STONE PLACED: ", stoneColor)
        self.stoneColor = stoneColor

    def getLiberties(self):
        return self.liberties

    def setLiberties(self, liberties):
        self.liberties = liberties

    def getBoardXPosition(self):
        return self.x

    def getBoardYPosition(self):
        return self.y

    def stoneAbove(self, boardArr):
        if self.y != 0:
            return boardArr[self.y - 1][self.x]

    def stoneBelow(self, boardArr):
        if self.y != 6:
            return boardArr[self.y + 1][self.x]

    def stoneRight(self, boardArr):
        if self.y != 6:
            return boardArr[self.y][self.x + 1]

    def stoneLeft(self, boardArr):
        if self.y != 0:
            return boardArr[self.y][self.x - 1]
