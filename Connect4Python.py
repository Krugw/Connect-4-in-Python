import sys
from itertools import chain

EMPTY = '.'
REDPLAYER = 'W'
BLACKPLAYER = 'B'

#Changes matrix to a positive diag (bottom-left to upper-right)
def diagonalsPos (matrix, col, row):
	for di in ([(j, i - j) for j in range(col)] for i in range(col + row -1)):
		yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < col and j < row]
		
#Changes matrix to a negitive diag (bottom-right to upper-left)
def diagonalsNeg (matrix, col, row):
	for di in ([(j, i - col + j + 1) for j in range(col)] for i in range(col + row - 1)):
		yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < col and j < row]

class Board:
        def __init__(self, col, row, winAmount):
                self.col = col
                self.row = row
                self.winAmount = winAmount
                self.board = [[EMPTY] * row for _ in range(col)]
        #If needed...
        def __str__(self):
                return "col: "+str(self.col)+". row: "+str(self.row)+". win: "+str(self.winAmount)+ "."+str(self.board)

        def placeToken(self, col, player):
                chosenCol = self.board[col]
                if chosenCol[0] != EMPTY:
                        raise BoardError("This Column is full!")
                i = -1
                while chosenCol[i] != EMPTY:
                        i -= 1
                chosenCol[i] = player

        def printBoard (self):
                print('  '.join(map(str, range(self.col))))
                for y in range(self.row):
                        print('  '.join(str(self.board[x][y]) for x in range(self.col)))
                print '\n'

        def winner(self, player):
                win = lambda x: ('\n'
                                +"###################"
                                +'\n'+x+" player wins!!"
                                +'\n'+"###################")
                if self.colWin(player) == 0:
                        print win(player)
                        return 0
                if self.rowWin(player) == 0:
                        print win(player)
                        return 0
                if self.diagPosWin(player) == 0:
                        print win(player)
                        return 0
                if self.diagNegWin(player) == 0:
                        print win(player)
                        return 0
                return 1
                
        def colWin(self, player):
                Counter = 0
                CTP = ''
                for a in self.board:
                        return scan(a, player)


        def rowWin(self, player):
                Counter = 0
                CTP = ''
                for a in zip(*self.board):
                        return scan(a, player)


        def diagPosWin(self, player):
                Counter = 0
                CTP = ''
                for a in diagonalsPos(self.board, self.col, self.row):
                        return scan(a, player)


        def diagNegWin(self, player):
                Counter = 0
                CTP = ''
                for a in diagonalsNeg(self.board, self.col, self.row):
                        return scan(a, player)

        def scan(self, matrix, player):
                for b in matrix:
                                if Counter == 0 and b != '.':
                                        Counter += 1
                                        CTP = b
                                if Counter > 0 and b!= '.':
                                        if CTP == b:
                                                Counter += 1
                                        else:
                                                Counter = 1
                                                CTP = b
                                if Counter == self.winAmount+1:
                                        return 0
                        Counter = 0
                        CTP = ''
                return 1

class BoardError(Exception):
        def __init__(self, arg):
                self.msg = arg
        
if __name__ == '__main__':
        #Trys to create new board
        try: game = Board(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

        #Following exceptions look to make sure there are:
        #enough sys args, sysargs are integers only and checks
        #col, row and win amount to be optimal
        except IndexError:
                print ("Invalid input! Make sure to add columns, rows and length to win in this format:"
                               +'\n'+"FILENAME.py NUMBEROFCOLUMNS NUMBEROFROWS LENGTHTOWIN"
                               +'\n'+"Ending Program...")
                raise SystemExit
        except ValueError:
                print ("Values are of wrong type!"
                               +'\n'+"Check to make sure col, row and length to win are of value integer"
                               +'\n'+"Ending Program...")
                raise SystemExit
        try:
                if game.col < 4:
                        raise BoardError("Coloumn size is too small! Coloumn size should be 4 or greater")
                elif game.row < 4:
                        raise BoardError("Row size is too small! Row size should be 4 or greater")
                elif game.winAmount < 3:
                        raise BoardError("Win amount is too small! Win size should be 3 or greater")
                elif game.winAmount > game.col:
                        raise BoardError("Win amount is too large!"
                                                     +'\n'+"Win size should be less than or equal to "
                                                     "coloumn amount")
        except BoardError, arg:
                print arg.msg
                print "Ending Program..."
                raise SystemExit
        #Sets up variables for gameplay
        finally:
                runningGame = 1
                turn = REDPLAYER
                playerPrint = "White"
                validToken = 0
                
        #START OF GAME
        print "WELCOME TO CONNECT 4 IN PYTHON!!"
        while runningGame == 1:
                game.printBoard()
                print playerPrint+" player, Enter coloumn: "
                while validToken == 0:
                        try:
                                tokenCol = input(">> ")
                                game.placeToken(tokenCol, turn)
                        except BoardError, arg:
                                print arg.msg
                                print "Enter a new column: "
                        except IndexError:
                                print "Not a valid column!"
                                print "Enter a new column: "
                        except NameError:
                                print "Not a valid column!"
                                print "Enter a new column: "
                        else: validToken = 1
                runningGame = game.winner(playerPrint)
                turn = BLACKPLAYER if turn == REDPLAYER else REDPLAYER
                playerPrint = "Black" if playerPrint == "White" else "White"
                validToken = 0

        game.printBoard()
        
                
