def main():
    #set up board
    board=[]
    for i in range(6):
        #height is 6
        board.append([])
        for j in range(7):
            #width is 7
            board[i].append("")
    print(board)


if(__name__=="__main__"):
    main()
