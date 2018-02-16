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
        self.gameWonBy=False
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
            self.switchPlayerTurn()

            #print end result
            print("TURN:"+str(self.numberOfTurnsPlayed))
            self.printBoard()
            self.numberOfTurnsPlayed+=1

            #check if the game have ended
            if(self.checkIfGameIsComplete()):
                print("The game have ended")
                gameWonBy=self.checkIfPlayerWon()
                if(gameWonBy!=False):
                    print("The game was won by "+gameWonBy)
                    self.gameWonBy=gameWonBy
                else:
                    print("The game was a draw")
        else:
            #move is illegal
            print(rejectMessage)
            return rejectMessage
        
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

    def switchPlayerTurn(self):
        playerTurn=self.playerTurn
        if (playerTurn=="R"):
            playerTurn="Y"
        else:
            playerTurn="R"
        self.playerTurn=playerTurn

    def checkIfPlayerWon(self):
        stack=["","","",""]
        #if game is not won by anywon then false is returend
        winner=False
        #check for horizontal victory
        for i in self.board:
            for j in range(len(i)):
                stack[j%4]=i[j]
                if(stack[0]==stack[1]==stack[2]==stack[3] and stack[0]!=" "):
                    winner=stack[0]
                    return winner
        stack=["","","",""]
        #check for vertical victory
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                stack[j%4]=self.board[j][i]
                if(stack[0]==stack[1]==stack[2]==stack[3] and stack[0]!=" "):
                    winner=stack[0]
                    return winner
        stack=["","","",""]
        #check for diagonal victory [top left to bottom right]
        for y in range(len(self.board)):
            stack=["","","",""]
            x=0 
            while(x <len(self.board[0]) and y<len(self.board)):
                stack[x%4]=self.board[y][x]
                if(stack[0]==stack[1]==stack[2]==stack[3] and stack[0]!=" "):
                    winner=stack[0]
                    return winner
                x+=1
                y+=1
        for x in range(len(self.board[0])):
            stack=["","","",""]
            y=0
            while(x <len(self.board[0]) and y<len(self.board)):
                stack[x%4]=self.board[y][x]
                if(stack[0]==stack[1]==stack[2]==stack[3] and stack[0]!=" "):
                    winner=stack[0]
                    return winner
                x+=1
                y+=1
        #check for diagonal victory [bottom left to top right]
        for y in range(len(self.board)):
            stack=["","","",""]
            x=0 
            while(x < len(self.board[0]) and y>=0):
                stack[x%4]=self.board[y][x]
                if(stack[0]==stack[1]==stack[2]==stack[3] and stack[0]!=" "):
                    winner=stack[0]
                    return winner
                x+=1
                y-=1
        for x in range(len(self.board[0])):
            stack=["","","",""]
            y=len(self.board)-1
            while(x <len(self.board[0]) and y>=0):
                stack[x%4]=self.board[y][x]
                if(stack[0]==stack[1]==stack[2]==stack[3] and stack[0]!=" "):
                    winner=stack[0]
                    return winner
                x+=1
                y-=1
        #game not won by anyone if it return false
        return False
    
    def checkIfGameIsComplete(self):
        board=self.board
        gameEnded=True
        #check if there are any " " inside the board
        for row in board:
            if (" " in row):
                gameEnded=False
                break
        #check if someone won the game
        if(self.checkIfPlayerWon()!=False):
            gameEnded=True
            
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

    def whoWonTheGame():
        #returns false if no one have won
        if(self.gameWonBy=="R"):
            player= "RED"
        elif(self.gameWonBy=="Y"):
            player= "YELLOW"
        else:
            player=False
        return player
