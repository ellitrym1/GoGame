from stone import stone


class game():
    turn = 1
    x = 0
    y = 0
    whiteStonesCaptured = 0
    whiteTerritories = 0
    blackStonesCaptured = 0
    blackTerritories = 0

    def getTurn(self):
        return self.turn

    def getBlackStonesCaptured(self):
        return self.blackStonesCaptured

    def getWhiteStonesCaptured(self):
        return self.whiteStonesCaptured

    def getBlackTerritories(self):
        return self.blackTerritories

    def getWhiteTerritories(self):
        return self.whiteTerritories

    def getBoardArr(self):
        return self.boardArr

    def vacant(self):
        if self.boardArr[self.y][self.x].getStoneColor() == 0:
            return True
        else:
            return False

    def placeStone(self):
        if self.turn == 1:
            self.boardArr[self.y][self.x].setStoneColor(1)
            self.changeTurn()
        else:
            self.boardArr[self.y][self.x].setStoneColor(2)
            self.changeTurn()

    def captureStone(self, x, y):
        if self.boardArr[y][x].getStoneColor() == 1:
            self.whiteStonesCaptured += 1
            self.boardArr[y][x] = stone(0, x, y)
        else:
            self.blackStonesCaptured += 1
            self.boardArr[y][x] = stone(0, x, y)

    def updateLiberties(self):
        count = 0
        for r in self.boardArr:
            for c in r:
                count = 0
                if c.getStoneColor() != 0:
                    stoneColor = c.getStoneColor()
                    if c.stoneAbove(self.boardArr) != None and (c.stoneAbove(self.boardArr).getStoneColor() == stoneColor or c.stoneAbove(self.boardArr).getStoneColor() == 0):
                        count += 1
                    if c.stoneBelow(self.boardArr) != None and (c.stoneBelow(self.boardArr).getStoneColor() == stoneColor or c.stoneBelow(self.boardArr).getStoneColor() == 0):
                        count += 1
                    if c.stoneRight(self.boardArr) != None and (c.stoneRight(self.boardArr).getStoneColor() == stoneColor or c.stoneRight(self.boardArr).getStoneColor() == 0):
                        count += 1
                    if c.stoneLeft(self.boardArr) != None and (c.stoneLeft(self.boardArr).getStoneColor() == stoneColor or c.stoneLeft(self.boardArr).getStoneColor() == 0):
                        count += 1
                    c.setLiberties(count)
                    # print(c.getLiberties())


    def removeStone(self):
        for r in self.boardArr:
            for c in r:
                if c.getLiberties == 0 and c.getStoneColor() != 0:
                    if c.getStoneColor() == 1:
                        self.blackStonesCaptured += 1
                        self.boardArr[c.y][c.x] = stone(0, c.x, c.y)
                    elif c.getStoneColor() == 2:
                        self.whiteStonesCaptured += 1
                        self.boardArr[c.y][c.x] = stone(0, c.x, c.y)

    def updateStonesCaptured(self):
        if self.boardArr[self.y][self.x].stoneAbove(self.boardArr) != None and self.boardArr[self.y][
            self.x].stoneAbove(self.boardArr).getLiberties == 0 and self.boardArr[self.y][
            self.x].stoneAbove(self.boardArr).getStoneColor != 0:
            return self.captureStone(self.x, self.y - 1)
        elif self.boardArr[self.y][self.x].stoneRight(self.boardArr) != None and self.boardArr[self.y][
            self.x].stoneRight(self.boardArr).getLiberties == 0 and self.boardArr[self.y][
            self.x].stoneRight(self.boardArr).getStoneColor != 0:
            return self.captureStone(self.x + 1, self.y)
        elif self.boardArr[self.y][self.x].stoneLeft(self.boardArr) != None and self.boardArr[self.y][
            self.x].stoneLeft(self.boardArr).getLiberties == 0 and self.boardArr[self.y][
            self.x].stoneLeft(self.boardArr).getStoneColor != 0:
            return self.captureStone(self.x - 1, self.y)
        elif self.boardArr[self.y][self.x].stoneBelow(self.boardArr) != None and self.boardArr[self.y][
            self.x].stoneBelow(self.boardArr).getLiberties == 0 and self.boardArr[self.y][
            self.x].stoneBelow(self.boardArr).getStoneColor != 0:
            return self.captureStone(self.x, self.y + 1)

    def updateTerritories(self):
        blackTerritory = 0
        whiteTerritory = 0
        for r in self.boardArr:
            for c in r:
                if c.getStoneColor() == 1:
                    blackTerritory += 1
                elif c.getStoneColor() == 2:
                    whiteTerritory += 1
        self.whiteTerritories = whiteTerritory
        self.blackTerritories = blackTerritory
        # print(self.boardArr[0][0].getStoneColor())


    def suicideRule(self):
        other = 0
        if self.turn == 1:
            other = 2
        else:
            other = 1
        count = 0
        if self.boardArr[self.y][self.x].stoneAbove(self.boardArr) == None or self.boardArr[self.y][
            self.x].stoneAbove(self.boardArr).getStoneColor() == other:
            count = count + 1
        if self.boardArr[self.y][self.x].stoneLeft(self.boardArr) == None or self.boardArr[self.y][
            self.x].stoneLeft(self.boardArr).getStoneColor() == other:
            count = count + 1
        if self.boardArr[self.y][self.x].stoneRight(self.boardArr) == None or self.boardArr[self.y][
            self.x].stoneRight(self.boardArr).getStoneColor() == other:
            count = count + 1
        if self.boardArr[self.y][self.x].stoneBelow(self.boardArr) == None or self.boardArr[self.y][
            self.x].stoneBelow(self.boardArr).getStoneColor() == other:
            count = count + 1

        if count == 4:
            if self.boardArr[self.y][self.x].stoneAbove(self.boardArr) != None and self.boardArr[self.y][
                self.x].stoneAbove(self.boardArr).getLiberties == 1:
                return False
            if self.boardArr[self.y][self.x].stoneLeft(self.boardArr) != None and self.boardArr[self.y][
                self.x].stoneLeft(self.boardArr).getLiberties == 1:
                return False
            if self.boardArr[self.y][self.x].stoneRight(self.boardArr) != None and self.boardArr[self.y][
                self.x].stoneRight(self.boardArr).getLiberties == 1:
                return False
            if self.boardArr[self.y][self.x].stoneBelow(self.boardArr) != None and self.boardArr[self.y][
                self.x].stoneBelow(self.boardArr).getLiberties == 1:
                return False
            return True
        else:
            return False

    def changeTurn(self):
        if self.turn == 1:
            self.turn = 2
            print("Turn changed to white")
        else:
            self.turn = 1
            print("Turn changed to black")

    def updateVars(self, x, y, boardArr):
        self.x = x
        self.y = y
        self.boardArr = boardArr
        print("x: ", x)
        print("y: ", y)