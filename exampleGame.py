"""An example program that demonstrates how connect4 moduel can be used
to generate a pvp connect4 game"""
import connect4
def main():
    myConnect4=connect4.Connect4()
    while(myConnect4.haveGameEnded()==False):
        lastMoveIsLegal=False
        while(lastMoveIsLegal==False):
            inputNum=eval(input(myConnect4.whosTurnIsIt() + " player, please enter input: "))
            myConnect4.makeMove(inputNum)
            lastMoveIsLegal=myConnect4.wasLastMoveLegal()
             
if(__name__=="__main__"):
    main()
