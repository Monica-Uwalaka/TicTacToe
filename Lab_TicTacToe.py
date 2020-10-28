class TicTacToe:
    def __init__(self):
        #"board" is a list of 10 strings representing the board (ignore index 0) #my question: why are we ignoring index 0
        self.board = [" "]*10
        self.board[0]="#"
        self.Wins= ((0, 1, 2),   #wins is a list of tuples with possible winning combinations 
           (3, 4, 5),
           (6, 7, 8),
           (0, 3, 6),
           (1, 4, 7),
           (2, 5, 8),
           (0, 4, 8),
           (2, 4, 6))          
    
    def drawBoard(self):
        # This method prints out the board with current plays adjacent to a board with index. 
        print ("{0} | {1} | {2} \t 7 | 8 | 9 \n----------\t-----------\n{3} | {4} | {5} \t 4 | 5 | 6 \n----------\t-----------\n{6} | {7} | {8} \t 1 | 2 | 3 \n"
               .format(self.board[7],self.board[8],self.board[9],self.board[4],self.board[5],self.board[6],self.board[1],self.board[2],self.board[3])) 
       
        # self_assignment:learn more about formatting in your free time, done
    
    def boardFull(self):
        #This method checks if the board is already full and returns True. Returns false otherwise
        if " " in self.board:
            return False
        else:
            return True

    
    def cellIsEmpty(self, cell):
        #This method checks if a cell is empty in the board
        if self.board[cell]==" ":
            return True
        else:
            return False    
    
    
    def assignMove(self, cell,ch):
        # assigns the cell of the board to the character ch
        self.board[cell] = ch
    
    
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""
   
    
    def isWinner(self, ch):
        # Given a player's letter, this method returns True if that player has won.
        #if ch= "x":
  
            if self.board[7] == self.board[8] == self.board[9]== ch:
                return True   
            elif self.board[4] == self.board[5] == self.board[6]== ch:
                return True  
            elif self.board[1] == self.board[2] == self.board[3]== ch:
                return True 
            elif self.board[7] == self.board[4] == self.board[1]== ch:
                return True 
            elif self.board[8] == self.board[5] == self.board[2]== ch:
                return True 
            elif self.board[1] == self.board[2] == self.board[3]== ch:
                return True  
            elif self.board[1] == self.board[5] == self.board[9]== ch:
                return True  
            elif self.board[7] == self.board[5] == self.board[3]== ch:
                return True             
                           
            
                       
def main():
    myBoard=TicTacToe()  #self_assignment: what does this assignment do?
    #construct instance of ttt class
    gameIsOn=True        # do you know why you made this assignment?
    turn='x'
    while gameIsOn:
    #draw the board
        myBoard.drawBoard()
        move='0'
        while not myBoard.cellIsEmpty(int(move)):  #why 
            move = '0'
            print('it is turn for:', turn)
            move=input("Enter a number:")
            
            if int(move) in range(1,10):
                break
        myBoard.assignMove(int(move),turn)
        winner=myBoard.whoWon()
        if winner != "":
            myBoard.drawBoard()
            print("{0} wins.congrats!\n".format(turn))
            gameIsOn=False
        elif myBoard.boardFull():
            myBoard.drawBoard()
            print("it's a tie.\n")
            gameIsOn=False
        elif turn=='x':
            turn='o'
        elif turn=='o':
            turn='x'    
    
  
main()






    
    
    
