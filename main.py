def setUpBoard():
    #set up board
    board=[]
    for i in range(6):
        #height is 6
        board.append([])
        for j in range(7):
            #width is 7
            board[i].append("")
    return board

def printBoard(board):
    for i in range(len(board)):
        print(board[i])
        
def main():
    board=setUpBoard()
    printBoard(board)

if(__name__=="__main__"):
    main()
