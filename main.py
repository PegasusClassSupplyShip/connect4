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

def validateMove(board,inputNum):
    horizontalBoardLength=len(board[0])
    rejectMesseage="no problem"
    if(type(inputNum)!=type(1)):
        #check if inpput is an integer
        rejectMesseage="please enter an integer"
    elif(inputNum<0 or inputNum>horizontalBoardLength-1):
         #check if input is inside board
        rejectMesseage="input is outside the board"
    else:
        #check if the selected board is full or not
        rejectMesseage="the selected row is full"
        for i in board:
            if(i[inputNum]==" "):
                rejectMesseage="no problem"
                break;
    return rejectMesseage

def checkIfGameIsComplete(board):
    gameEnded=True
    #check if there are any " " inside the board
    for row in board:
        if (" " in row):
            gameEnded=False
            break
    return gameEnded
    
def main():
    board=setUpBoard()
    print("TURN:0")
    printBoard(board)
    gameEnded=False
    #plater turn is "R" or "Y" for red or yellow
    playerTurn="R"
    numberOfTurnsPlayed=0
    while(gameEnded==False):
        #getInPut / validate move
        rejectMessage=""
        while(rejectMessage!="no problem"):
            print(rejectMessage)
            inputNum=eval(input(playerTurn + " player, please enter input: "))
            rejectMessage=validateMove(board,inputNum)
            
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
        #check if game have ended
        gameEnded=checkIfGameIsComplete(board)
        if(gameEnded):
            print("The game have ended")
if(__name__=="__main__"):
    main()
