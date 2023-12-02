from Player import Player
from gameLogic import  numOf4Connected, insertMove, result, isGameFull
import copy
class ComputerPlayer(Player):
    def __init__(self, playerSym, otherSym):  
        super().__init__(playerSym, otherSym)
        
    def possibleMoves(self,playerSym, boardState):
        # return all possible moves
        possibleMoves_cols = []
        for i in range(len(boardState)):
            tempState = copy.deepcopy(boardState)
            if(tempState[i][0] == 0):
                possibleState_col = insertMove(i, playerSym, tempState)
                if(possibleState_col != None):
                    possibleMoves_cols.append(possibleState_col)
        return possibleMoves_cols

    def getMax(self, otherPlayerSym, possibleMoves_cols,depth):
        # @ returns the maximum possible move
        maxCol_value = (float('-inf'), None)
        depth += 1
        for boardState,col in possibleMoves_cols:
            temp_value= max(maxCol_value[0], self.getMove(otherPlayerSym, boardState,depth)[0])
            if maxCol_value[0] < temp_value:
                maxCol_value = temp_value,col
        return maxCol_value  


    def getMin(self, otherPlayerSym, possibleMoves_cols,depth):
        # @ returns the minimum possible move
        print("depth(min): " + str(depth))
        minCol_value = (float('inf'), None)
        depth += 1
        for boardState,col in possibleMoves_cols:
            temp_value= min(minCol_value[0], self.getMove(otherPlayerSym, boardState,depth)[0])
            if minCol_value[0] > temp_value:
                minCol_value = temp_value,col
        return minCol_value

    def getMove(self, playerSym, boardState,depth):
        #print(depth)
        if(isGameFull(boardState)):
            return result(boardState, self.sym, self.otherSym),None
        if(depth >= 3):
            return result(boardState, self.sym, self.otherSym),None
        possibleMoves_cols = self.possibleMoves(playerSym, boardState)
        if(playerSym == self.sym):
            return self.getMin(self.otherSym, possibleMoves_cols,depth)
        else:
            return self.getMax(self.sym, possibleMoves_cols, depth)

