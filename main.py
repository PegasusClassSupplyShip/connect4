class Connect4:
    
    def __init__(self,horiLength=7,vertLength=6):
        self.horiLength=horiLength
        self.vertLength=vertLength
        self.board=self.setUpBoard()
        #plater turn is "R" or "Y" for red or yellow
        self.playerTurn="R"
        #will return no problem if the move is legal
        self.legalMoveRejectMessage="no problem"
        self.lastInputWasLegal=False
        self.gameEnded=self.checkIfGameIsComplete()
        self.numberOfTurnsPlayed=0

        print("TURN:0")
        self.printBoard()
    
    def setUpBoard(self):
        #set up board
        board=[]
        for i in range(self.vertLength):
            #generate layers of list
            board.append([])
            for j in range(self.horiLength):
                #generate width
                board[i].append(" ")
        return board

    def printBoard(self):
        board=self.board
        #display board
        horizontalIndex=[]
        for i in range(len(board[0])):
            horizontalIndex.append(str(i))
        print(" ",horizontalIndex)
        for i in range(len(board)):
            print(str(i), board[i])

    def makeMove(self,inputNum):
        #validate move
        rejectMessage=self.validateMove(inputNum)
        if(rejectMessage==self.legalMoveRejectMessage):
            #move was valid
            board=self.board
            playerTurn=self.playerTurn
            deepestIndex=len(board)-1
            chipPlaced=False
            while(chipPlaced==False):
                if(board[deepestIndex][inputNum]==" "):
                    board[deepestIndex][inputNum]=playerTurn
                    chipPlaced=True
                deepestIndex-=1
            self.board=board
            #switch the player who is about to make a move
            self.switchPlaterTurn()
        else:
            #move is illegal
            print(rejectMessage)
            return rejectMessage

        self.checkIfGameIsComplete();
        if(self.checkIfGameIsComplete()):
            print("The game have ended")

        #print end result
        print("TURN:"+str(self.numberOfTurnsPlayed))
        self.printBoard()
        
    def validateMove(self,inputNum):
        board=self.board
        horizontalBoardLength=len(board[0])
        rejectMessage=self.legalMoveRejectMessage
        if(type(inputNum)!=type(1)):
            #check if inpput is an integer
            rejectMessage="please enter an integer"
        elif(inputNum<0 or inputNum>horizontalBoardLength-1):
             #check if input is inside board
            rejectMessage="input is outside the board"
        else:
            #check if the selected board is full or not
            rejectMessage="the selected row is full"
            for i in board:
                if(i[inputNum]==" "):
                    rejectMessage=self.legalMoveRejectMessage
                    break;
                
        #set attributes of validation
        self.lastInputWasLegal = (rejectMessage=="no problem")
        return rejectMessage

    def switchPlaterTurn(self):
        playerTurn=self.playerTurn
        if (playerTurn=="R"):
            playerTurn="Y"
        else:
            playerTurn="R"
        self.playerTurn=playerTurn

    def checkIfGameIsComplete(self):
        board=self.board
        gameEnded=True
        #check if there are any " " inside the board
        for row in board:
            if (" " in row):
                gameEnded=False
                break
        self.gameEnded = gameEnded
        return(gameEnded)

    #exist for encapsulation of the class
    def wasLastMoveLegal(self):
        return self.lastInputWasLegal
    
    def haveGameEnded(self):
        return self.gameEnded

    #returns whos turn it is to play
    def whosTurnIsIt(self):
        if (self.playerTurn=="R"):
            player= "RED"
        else:
            player= "YELLOW"
        return player
    
def main():
    myConnect4=Connect4()
    while(myConnect4.haveGameEnded()==False):
        lastMoveIsLegal=False
        while(lastMoveIsLegal==False):
            inputNum=eval(input(myConnect4.whosTurnIsIt() + " player, please enter input: "))
            myConnect4.makeMove(inputNum)
            lastMoveIsLegal=myConnect4.wasLastMoveLegal()
            
if(__name__=="__main__"):
    main()
