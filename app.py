import copy
class Connect4Game:
    def __init__(self):
        # Initialize the game variables
        self.player1sym = 1
        self.player2sym = 0
        self.player1Score = 0
        self.player2Score = 0
        self.length = 6
        self.width = 7
        self.game = [[-1 for _ in range(self.length)] for _ in range(self.width)]

    def isColFull(self, col):
        # Check if a column is full
        return self.game[col][0] != -1

    def isGameFull(self):
        # Check if the game board is full
        lresult = True
        for i in range(self.width):
            lresult = lresult and self.isColFull(i)
        return lresult

    def increaseScore(self, playerSym):
        # Increase the score of the specified player
        if (playerSym == self.player1sym):
            self.player1Score += 1
        else:
            self.player2Score += 1
        pass

    def numOf4Connected(self, playerSym, gameState=None):
        # Calculate the number of 4 connected pieces in the game board    
        currentState = None
        if(gameState == None):
            currentState = self.game
        else: 
            currentState = gameState
        count = 0
        for col in range(self.width):
            for row in range(self.length):
                flag = True
                if(row + 3 < self.length):
                    for i in range(0, 4):   
                        #print(str(row+i) +"-->"+ str(currentState[col][row+ i]))
                        flag = flag and (currentState[col][row+ i]== playerSym)
                    if(flag):
                        count += 1
                if(col - 4 >= 0):
                    flag = True
                    for i in range(4):
                        flag = flag and (currentState[col-i][row] == playerSym)
                    if(flag):
                        count += 1
                if(col + 4  <= self.width):
                    flag = True
                    for i in range(4):
                        flag = flag and (currentState[col+i][row] == playerSym)
                    if(flag):
                        count += 1
                if((col + 4  <= self.width) and (row + 4 <= self.length)):
                    flag = True
                    for i in range(4):
                        flag  = flag and (currentState[col+i][row+i] == playerSym)
                    if(flag):
                        count += 1
        return count
    
    def possibleMoves(self, playerSym, gameState):
        # return all possible moves
        temp = []
        for i in range(self.width):
            currentState =  copy.deepcopy(gameState)
            if(currentState[i][0] == -1):
                temp.append(self.insertMove(i, playerSym, currentState))
        return temp
    
    def result(self, gameState=None):
        # result the result fo the game
        self.player1Score = self.numOf4Connected(self.player1sym, gameState)
        self.player2Score = self.numOf4Connected(self.player2sym, gameState)
        if(self.player1Score > self.player2Score):
            print ("player 1")
        else:
            print("player 2")
    
    def insertMove(self,col , playerSym, gameState=None):
        # insert a new move 
        if(gameState != None):
            # insert new move in givven game state
            row = self.getHiestEmptyCell(col, gameState)
            if row is not None:
                gameState[col][row] = playerSym
            return gameState
        else:
            row = self.getHiestEmptyCell(col, self.game)
            if row is not None:
                self.game[col][row] = playerSym
        return gameState
    
    def getHiestEmptyCell(self, col, gameState):
        for i in range(self.length-1,-1,-1):
            if(gameState[col][i] == -1):
                return i
        return None

""" tempGame = Connect4Game()
print("isGameFull: "+  str(tempGame.isGameFull()))
print("player1 Score " + str(tempGame.player1Score))
tempGame.increaseScore(tempGame.player1sym)
print("player1 Score " + str(tempGame.player1Score))
#print("number of 4 connecter"+ str(tempGame.possibleMoves(tempGame.player1sym, tempGame.game)))
print(tempGame.getHiestEmptyCell(0, tempGame.game))
tempGame.insertMove(0, tempGame.player1sym)
tempGame.insertMove(0, tempGame.player1sym)
tempGame.insertMove(0, tempGame.player1sym)
print(tempGame.game)
count = tempGame.possibleMoves(tempGame.player2sym, tempGame.game)
tempGame.insertMove(1, tempGame.player2sym)
tempGame.insertMove(3, tempGame.player2sym)
count2 = tempGame.possibleMoves(tempGame.player1sym, tempGame.game)
for x in count:
    print(x)
    print("")
for x in count2:
    print(x)
    print("") """
tempGame = Connect4Game()
tempGame.insertMove(1, tempGame.player2sym)
tempGame.insertMove(1, tempGame.player2sym)
tempGame.insertMove(1, tempGame.player2sym)
tempGame.insertMove(1, tempGame.player2sym)
print(tempGame.numOf4Connected(tempGame.player2sym))