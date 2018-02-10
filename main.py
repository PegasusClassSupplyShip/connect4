def setUpBoard():
    #set up board
    board=[]
    for i in range(6):
        #height is 6
        board.append([])
        for j in range(7):
            #width is 7
            board[i].append(" ")
    return board

def printBoard(board):
    #display board
    horizontalIndex=[]
    for i in range(len(board[0])):
        horizontalIndex.append(str(i))
    print(" ",horizontalIndex)
    for i in range(len(board)):
        print(str(i), board[i])

def makeMove(playerTurn,inputNum,board):
    deepestIndex=len(board)-1
    chipPlaced=False
    while(chipPlaced==False):
        if(board[deepestIndex][inputNum]==" "):
            board[deepestIndex][inputNum]=playerTurn
            chipPlaced=True
        deepestIndex-=1
    return board

def main():
    board=setUpBoard()
    print("TURN:0")
    printBoard(board)
    gameEnded=False
    #plater turn is "R" or "Y" for red or yellow
    playerTurn="R"
    numberOfTurnsPlayed=0
    while(gameEnded==False):
        #getInPut
        inputNum=eval(input(playerTurn + " player, please enter input: "))
        #makeMove
        board=makeMove(playerTurn,inputNum,board)
        #printBoard
        print("")
        numberOfTurnsPlayed+=1
        print("TURN:",numberOfTurnsPlayed)
        printBoard(board)
        if (playerTurn=="R"):
            playerTurn="Y"
        else:
            playerTurn="R"
            
if(__name__=="__main__"):
    main()
