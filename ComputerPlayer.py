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

    def getMax(self, otherPlayerSym, possibleMoves_cols,depth, isPruning, alpha, beta):
        # @ returns the maximum possible move
        #print("depth(max): " + str(depth))
        maxCol_value = (float('-inf'), None)
        depth += 1
        for boardState,col in possibleMoves_cols:
            if(isPruning and alpha >= beta):
                continue
            temp_value = max(maxCol_value[0], self.getMove(otherPlayerSym, boardState,depth, isPruning, alpha, beta)[0])
            if(isPruning):
                alpha = max(alpha, temp_value)
            if maxCol_value[0] < temp_value:
                maxCol_value = temp_value,col
        return maxCol_value  


    def getMin(self, otherPlayerSym, possibleMoves_cols,depth, isPruning, alpha, beta):
        # @ returns the minimum possible move
        #print("depth(min): " + str(depth))
        minCol_value = (float('inf'), None)
        depth += 1
        for boardState,col in possibleMoves_cols:
            if(isPruning and alpha >= beta):
                continue
            temp_value = min(minCol_value[0], self.getMove(otherPlayerSym, boardState,depth, isPruning, alpha, beta)[0])
            if(isPruning):
              beta = min(temp_value, beta)
            if minCol_value[0] > temp_value:
                minCol_value = temp_value,col
        #print("col: " + str(col))
        return minCol_value

    def getMove(self, playerSym, boardState,depth, isPruning, alpha=float('-inf'), beta=float('inf')):
        ##print(depth)
        if(isGameFull(boardState)):
            return numOf4Connected(playerSym, boardState),None
        if(depth >= 3):
            #print("game is at max depth --> player: " + str(playerSym) + "numofconnected4: "+ str(numOf4Connected(playerSym, boardState)))
            return numOf4Connected(playerSym, boardState),None
        possibleMoves_cols = self.possibleMoves(playerSym, boardState)
        if(playerSym == self.sym):
            return self.getMax(self.sym, possibleMoves_cols, depth, isPruning,alpha, beta)
        else:
            return self.getMin(self.otherSym, possibleMoves_cols,depth, isPruning, alpha, beta)
            

