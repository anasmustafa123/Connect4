def isColFull(col, boardState):
    # Check if a column is full
    return boardState[col][0] != 0

def isGameFull(boardState):
    # Check if the game board is full
    lresult = True
    for i in range(len(boardState)):
        lresult = lresult and isColFull(i, boardState)
    return lresult

def numOf4Connected(playerSym, boardState):
    # Calculate the number of 4 connected pieces in the game board    
    count = 0
    for col in range(len(boardState)):
        for row in range(len(boardState[0])):
            flag = True
            if(row + 3 < len(boardState[0])):
                for i in range(0, 4):   
                    flag = flag and (boardState[col][row+ i]== playerSym)
                if(flag):
                    count += 1
            if(col - 4 >= 0):
                flag = True
                for i in range(4):
                    flag = flag and (boardState[col-i][row] == playerSym)
                if(flag):
                    count += 1
            if(col + 4  <= len(boardState)):
                flag = True
                for i in range(4):
                    flag = flag and (boardState[col+i][row] == playerSym)
                if(flag):
                    count += 1
            if((col + 4  <= len(boardState)) and (row + 4 <= len(boardState[0]))):
                flag = True
                for i in range(4):
                    flag  = flag and (boardState[col+i][row+i] == playerSym)
                if(flag):
                    count += 1
    return count

def result(boardState, player1Sym, player2Sym):
    # result the result fo the game
    player1Score = numOf4Connected(player1Sym, boardState)
    player2Score = numOf4Connected(player2Sym, boardState)
    if(player1Score > player2Score):
        return 1
    elif(player1Score == player2Score):
        return 0
    else:
        return -1

def insertMove(col , playerSym, boardState):
    # insert new move in givven game state
    row = getHiestEmptyCell(col, boardState)
    if row is not None:
        boardState[col][row] = playerSym
        return boardState, col
    return None

def getHiestEmptyCell(col, boardState):
    for i in range(len(boardState[0])-1,-1,-1):
        if(boardState[col][i] == 0):
            return i
    return None