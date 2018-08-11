from os import system, name
from colorama import Fore, Style, Back, init

dwarfColor = Fore.BLUE
trollColor = Fore.RED
edgeColor = Back.WHITE
edgeFillColor = Fore.BLACK
edgeFill = edgeFillColor + " X "
rightPadding = " " * 20
borderColor = Back.WHITE
borderTextColor = Fore.RED
class Piece:
    """ Class dealing with default methods across all pieces. """
    def __init__(self, owner, position):
        self.position = position
        self.owner = owner

class Dwarf(Piece):
    """ Class that extends piece that deals with the Dwarf's capabilities. """
    def __init__(self, owner, position):
        Piece.__init__(self, owner, position)
        self.symbol = dwarfColor+" D "
        self.name = "Dwarf"
        self.points = 1
    def isValidMove(self, position, board):           
        """ Checks if the inputted position is a valid move. """
        if position in board.edges:
            return False
        increment = 1        
        if position in board.boardDict.keys() and board.boardDict[position].name == "Dwarf":
            return False
        if position not in board.boardDict.keys():
            if position[1:] == self.position[1:]:#horizontal
                if "ABCDEFGHIJKLMNO".index(position[0]) < "ABCDEFGHIJKLMNO".index(self.position[0]):
                    increment = -1         
                for i in range("ABCDEFGHIJKLMNO".index(self.position[0]), "ABCDEFGHIJKLMNO".index(position[0]), increment):
                    if board.getCoordinateSign("ABCDEFGHIJKLMNO"[i]+position[1:]) != "   ":
                        if ("ABCDEFGHIJKLMNO"[i]+position[1:]) != self.position and ("ABCDEFGHIJKLMNO"[i]+position[1:]) != position:
                            return False            
                #raw_input(self.position+" "+position)
                return True
            if position[0] == self.position[0]:#vertical
                if int(position[1:]) > int(self.position[1:]):
                    increment = -1
                
                for i in range(int(position[1:]), int(self.position[1:]), increment):
                    #print i
                    #raw_input(1)
                    if board.getCoordinateSign(position[0]+str(i)) != "   ":
                        return False 
                return True
            try:
                direction = [1, 1]#increment in [h, v] horizontal, vertical
                direction[0] = -("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0]))/abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0]))
                direction[1] = -(int(self.position[1:])-int(position[1:]))/abs(int(self.position[1:])-int(position[1:]))
                if abs(int(self.position[1:])-int(position[1:])) == abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0])):
                    for i in range(1, abs(int(self.position[1:])-int(position[1:]))):
                        if board.getCoordinateSign("ABCDEFGHIJKLMNO"["ABCDEFGHIJKLMNO".index(self.position[0])+(i*direction[0])]+str(int(self.position[1:])+(i*direction[1]))) != "   ":
                            return False
                    return True
                return False
            except ZeroDivisionError:
                return False
        if position in board.boardDict.keys() and board.boardDict[position].name == "Troll":
            if position[1:] == self.position[1:]:#horizontal
                if "ABCDEFGHIJKLMNO".index(position[0]) < "ABCDEFGHIJKLMNO".index(self.position[0]):
                    increment = -1                
                for i in range("ABCDEFGHIJKLMNO".index(self.position[0]), "ABCDEFGHIJKLMNO".index(position[0]), increment):
                    if board.getCoordinateSign("ABCDEFGHIJKLMNO"[i]+position[1:]) != "   ":
                        if ("ABCDEFGHIJKLMNO"[i]+position[1:]) != self.position and ("ABCDEFGHIJKLMNO"[i]+position[1:]) != position:
                            return False            
                dist = abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0]))
                for i in range(dist):
                    try:
                        if "ABCDEFGHIJKLMNO"["ABCDEFGHIJKLMNO".index(self.position[0])-(increment*i)]+str(self.position[1:]) not in board.boardDict.keys():
                            return False
                    except IndexError:
                        return False
                return True   
            if position[0] == self.position[0]:#vertical
                if int(position[1:]) < int(self.position[1:]):
                    increment = -1
                for i in range(int(position[1:]), int(self.position[1:]), increment):
                    if board.getCoordinateSign(position[0]+str(i)) != "   ":
                        return False 
                dist = abs(int(self.position[1:])-int(position[1:]))
                for i in range(dist):
                    try:
                        if position[0]+str(int(self.position[1:])-(increment*i)) not in board.boardDict.keys():
                            return False
                    except IndexError:
                        return False
                
                return True            
            try:
                direction = [1, 1]#increment in [h, v] horizontal, vertical
                direction[0] = -("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0]))/abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0]))
                direction[1] = -(int(self.position[1:])-int(position[1:]))/abs(int(self.position[1:])-int(position[1:]))
                reverseDirection = [-direction[0], -direction[1]]
                dist = abs(int(self.position[1:])-int(position[1:]))
                if abs(int(self.position[1:])-int(position[1:])) == abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0])):
                    for i in range(1, abs(int(self.position[1:])-int(position[1:]))):
                        if board.getCoordinateSign("ABCDEFGHIJKLMNO"["ABCDEFGHIJKLMNO".index(self.position[0])+(i*direction[0])]+str(int(self.position[1:])+(i*direction[1]))) != "   ":
                            return False
                    for i in range(dist):
                        if "ABCDEFGHIJKLMNO"["ABCDEFGHIJKLMNO".index(self.position[0])+(reverseDirection[0]*i)]+str(int(self.position[1:])+(reverseDirection[1]*i)) not in board.boardDict.keys():
                            return False
                    return True
                return False
            except ZeroDivisionError:
                return False            
            
            return True
        return False
    def movePiece(self, position, board):
        " Moves the piece."
        if position in board.boardDict.keys() and board.boardDict[position].name == "Troll":
            self.owner.otherPlayer.pieces.remove(board.boardDict[position])            
            self.owner.otherPlayer.points = sum(piece.points for piece in self.owner.otherPlayer.pieces)

        self.position = position
        board.NoTheWorldMustBePeopled()
class Troll(Piece):
    """ Class that extends piece that deals with the Troll's capabilities. """
    def __init__(self, owner, position):
        Piece.__init__(self, owner, position)
        self.symbol = trollColor+" T "
        self.name = "Troll"
        self.points = 4
    def isValidMove(self, position, board):           
        """ Checks if the inputted position is a valid move. """        
        if position in board.boardDict or position in board.edges:
            return False
        if (abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0])) <= 1) and (abs(int(self.position[1:])-int(position[1:])) <= 1):                    
            return True    
        else:                
            surroundingDwarfs = []
            for iterPosition in [letter + str(number) for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] for letter in "ABCDEFGHIJKLMNO"]:         
                if (abs("ABCDEFGHIJKLMNO".index(position[0])-"ABCDEFGHIJKLMNO".index(iterPosition[0])) <= 1) and (abs(int(position[1:])-int(iterPosition[1:])) <= 1) and iterPosition in board.boardDict.keys() and board.boardDict[iterPosition].name == "Dwarf":
                    surroundingDwarfs.append(iterPosition)
            if len(surroundingDwarfs) > 0:
                increment = 1
                if position[1:] == self.position[1:]:#horizontal
                    if "ABCDEFGHIJKLMNO".index(position[0]) < "ABCDEFGHIJKLMNO".index(self.position[0]):
                        increment = -1                
                    for i in range("ABCDEFGHIJKLMNO".index(self.position[0]), "ABCDEFGHIJKLMNO".index(position[0]), increment):
                        if board.getCoordinateSign("ABCDEFGHIJKLMNO"[i]+position[1:]) != "   ":
                            if ("ABCDEFGHIJKLMNO"[i]+position[1:]) != self.position and ("ABCDEFGHIJKLMNO"[i]+position[1:]) != position:
                                return False            
                    dist = abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0]))
                    for i in range(dist):
                        try:
                            if "ABCDEFGHIJKLMNO"["ABCDEFGHIJKLMNO".index(self.position[0])-(increment*i)]+str(self.position[1:]) not in board.boardDict.keys():
                                return False
                        except IndexError:
                            return False
                    return True   
                if position[0] == self.position[0]:#vertical
                    if int(position[1:]) < int(self.position[1:]):
                        increment = -1
                    for i in range(int(position[1:]), int(self.position[1:]), increment):
                        if board.getCoordinateSign(position[0]+str(i)) != "   ":
                            return False 
                    dist = abs(int(self.position[1:])-int(position[1:]))
                    for i in range(dist):
                        try:
                            if position[0]+str(int(self.position[1:])-(increment*i)) not in board.boardDict.keys():
                                return False
                        except IndexError:
                            return False
                    
                    return True            
                try:
                    direction = [1, 1]#increment in [h, v] horizontal, vertical
                    direction[0] = -("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0]))/abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0]))
                    direction[1] = -(int(self.position[1:])-int(position[1:]))/abs(int(self.position[1:])-int(position[1:]))
                    reverseDirection = [-direction[0], -direction[1]]
                    dist = abs(int(self.position[1:])-int(position[1:]))
                    if abs(int(self.position[1:])-int(position[1:])) == abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(position[0])):
                        for i in range(1, abs(int(self.position[1:])-int(position[1:]))):
                            if board.getCoordinateSign("ABCDEFGHIJKLMNO"["ABCDEFGHIJKLMNO".index(self.position[0])+(i*direction[0])]+str(int(self.position[1:])+(i*direction[1]))) != "   ":
                                return False
                        for i in range(dist):
                            if "ABCDEFGHIJKLMNO"["ABCDEFGHIJKLMNO".index(self.position[0])+(reverseDirection[0]*i)]+str(int(self.position[1:])+(reverseDirection[1]*i)) not in board.boardDict.keys():
                                return False
                        return True
                    return False
                except ZeroDivisionError:
                    return False            
             
                #return True            
        return False
    def movePiece(self, position, board):
        " Moves the piece."
        self.position = position
        for iterPosition in [letter + str(number) for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] for letter in "ABCDEFGHIJKLMNO"]:         
            if (abs("ABCDEFGHIJKLMNO".index(self.position[0])-"ABCDEFGHIJKLMNO".index(iterPosition[0])) <= 1) and (abs(int(self.position[1:])-int(iterPosition[1:])) <= 1) and iterPosition in board.boardDict.keys() and board.boardDict[iterPosition].name == "Dwarf":                    
                self.owner.otherPlayer.pieces.remove(board.boardDict[iterPosition])
                self.owner.otherPlayer.points = sum(piece.points for piece in self.owner.otherPlayer.pieces)

        board.NoTheWorldMustBePeopled()    
class Player:                         
    """ Class that deals with player data. """
    def __init__(self, board, side):
        self.side = side
        self.board = board
        self.capturedPieces = []
        self.otherPlayer = False
        if self.side == "Dwarf":
            self.pieces = (
                [
                    Dwarf(self, "F1"), Dwarf(self, "G1"), Dwarf(self, "I1"), Dwarf(self, "J1"),
                    Dwarf(self, "F15"), Dwarf(self, "G15"), Dwarf(self, "I15"), Dwarf(self, "J15"),
                    Dwarf(self, "A6"), Dwarf(self, "A7"), Dwarf(self, "A9"), Dwarf(self, "A10"),
                    Dwarf(self, "O6"), Dwarf(self, "O7"), Dwarf(self, "O9"), Dwarf(self, "O10")
                    ] +
                [Dwarf(self, "ABCDEFGHIJKLMNO"[i+10]+str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15][i+1])) for i in range(4)] +
                [Dwarf(self, "ABCDEFGHIJKLMNO"[i]+str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15][i+9])) for i in range(4, 0, -1)] +
                [Dwarf(self, "ABCDEFGHIJKLMNO"[i+1]+str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15][::-1][i+10])) for i in range(4)] +
                [Dwarf(self, "ABCDEFGHIJKLMNO"[i+10]+str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15][::-1][i+1])) for i in range(4)]
            )
        else:
            self.pieces = [Troll(self, "G9"), Troll(self, "G8"), Troll(self, "G7"), Troll(self, "I9"), Troll(self, "I8"), Troll(self, "I7"), Troll(self, "H9"), Troll(self, "H7")]
        self.points = sum(piece.points for piece in self.pieces)
    def loadOtherPlayer(self, board):
        " Initializes the player's other player instance . "
        self.otherPlayer = [p for p in board.players if p != self][0]  
class Board:    
    """ The board. """
    def __init__(self):
        self.gameWon = False
        self.board = []
        self.players = [Player(self, "Dwarf"), Player(self, "Troll")]
        for player in self.players:
            player.loadOtherPlayer(self)
        self.boardDict = {}
        self.NoTheWorldMustBePeopled()
        self.depth = 3
        self.count = 0
        self.edges = (
            ["ABCDE"[char]+str([11, 12, 13, 14, 15][num]) for char in range(len("ABCDE")) for num in range(char, len([1, 2, 3, 4, 5]))]+
            ["ABCDE"[char]+str([5, 4, 3, 2, 1][num]) for char in range(len("ABCDE")) for num in range(char, len([1, 2, 3, 4, 5]))]+
            ["ONMLK"[char]+str([5, 4, 3, 2, 1][num]) for char in range(len("ABCDE")) for num in range(char, len([1, 2, 3, 4, 5]))]+
            ["ONMLK"[char]+str([11, 12, 13, 14, 15][num]) for char in range(len("ABCDE")) for num in range(char, len([1, 2, 3, 4, 5]))]+["H8"]
        
        )    

    def printBoard(self):
        """ Prints out the chess board. """
        print "\n"
        print rightPadding + borderColor + borderTextColor + "[  ]" + ("[ ]" * 16) + Style.RESET_ALL
        for i in range(len(self.board)-1):   
            print rightPadding + colorRow(self.board[i], i+1, self)
        print rightPadding  + borderColor + borderTextColor + "".join(self.board[15]).encode("utf-8") + "[ ]" + Style.RESET_ALL
    def NoTheWorldMustBePeopled(self):#much ado about nothing -benedick
        """ Updates the player positions on the board. """
        self.boardDict = {}
        self.board = []
        for i in range(15, 0, -1):
            if i < 10:
                row = ["["+str(i)+" ]"]
            else:
                row = ["["+str(i)+"]"]
            row += (["   "] * 15)
            self.board.append(row)
        self.board.append(["[  ]", "[A]", "[B]", "[C]", "[D]", "[E]", "[F]", "[G]", "[H]", "[I]", "[J]", "[K]", "[L]", "[M]", "[N]", "[O]"])
        for player in self.players:
            for piece in player.pieces:
                self.changeCoordinateSign(piece.position, piece.symbol)
                self.boardDict[piece.position] = piece
    def getCoordinateSign(self, spot):
        """ Gets the coordinate sign of the inputted spot. """
        return self.board[15-int(spot[1:])][self.board[15].index("["+str(spot[0]).upper()+"]")]
    def changeCoordinateSign(self, spot, sign):
        """ Change the coordinate sign of the inputted spot. """
        self.board[15-int(spot[1:])][self.board[15].index("["+str(spot[0]).upper()+"]")] = sign

    def takeTurns(self):
        """ 
        Alternate between the players and moves.
        """
        while self.gameWon is False:
            for player in self.players:
                while self.gameWon is False:
                    try:
                        clear()
                        if len(player.otherPlayer.pieces) == 0:
                            self.gameWon = True
                            print " You have won!"
                            raw_input("Press enter to continue->")
                            break
                        self.printBoard()
                        print "\nCaptured Pieces:" 
                        for p in self.players:
                            print p.side+" Points  =  "+str(p.points)
                        print "\n"+player.side +"'s Turn!"
                        
                        piecePosition = raw_input("Please choose one of your pieces(ex:A2)\n->").rstrip("\r").upper()
                        if self.boardDict[piecePosition].name != player.side:
                            raise ValueError
                        correctPiece = raw_input("You have chosen your "+self.boardDict[piecePosition].name+" at "+piecePosition+". Is this correct(y/n)?\n->")
                        if correctPiece[0].upper() == "Y":
                            newPiecePosition = raw_input("Where would you like to move it?\n->").rstrip("\r").upper()
                            correctPieceMove = raw_input("You have chosen to move your "+self.boardDict[piecePosition].name+" from "+piecePosition+" to "+newPiecePosition+". Is this correct(y/n)?\n->")
                            if correctPieceMove[0].upper() == "Y" and self.boardDict[piecePosition].isValidMove(newPiecePosition, self):
                                self.boardDict[piecePosition].movePiece(newPiecePosition, self)
                            else:
                                raise ValueError
                        else:
                            raise ValueError
                    except (ValueError, KeyError, IndexError):
                        pass
                    else:
                        break
                            

def colorRow(row, rowNum, board):
    """ Returns a colored version of the inputted row. """
    reversedRowNum = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1][rowNum-1]
    colorRowList = []
    colorRowList.append(borderColor + borderTextColor + row[0] + Style.RESET_ALL)
    for i in range(1, len(row), 2):
        try:
            if rowNum % 2 == 0:
                if "ABCDEFGHIJKLMNO"[i-1]+str(reversedRowNum) not in board.edges:
                    colorRowList.append(Back.BLACK+row[i]+Style.RESET_ALL)
                else:
                    colorRowList.append(edgeColor+edgeFill+Style.RESET_ALL)
                if "ABCDEFGHIJKLMNO"[i]+str(reversedRowNum) not in board.edges:
                    colorRowList.append(Back.WHITE+row[i+1]+Style.RESET_ALL)
                else:
                    colorRowList.append(edgeColor+edgeFill+Style.RESET_ALL)
            else:
                if "ABCDEFGHIJKLMNO"[i-1]+str(reversedRowNum) not in board.edges:
                    colorRowList.append(Back.WHITE+row[i]+Style.RESET_ALL)
                else:
                    colorRowList.append(edgeColor+edgeFill+Style.RESET_ALL)
                if "ABCDEFGHIJKLMNO"[i]+str(reversedRowNum) not in board.edges:
                    colorRowList.append(Back.BLACK+row[i+1]+Style.RESET_ALL)  
                else:
                    colorRowList.append(edgeColor+edgeFill+Style.RESET_ALL)  
        except IndexError:
            pass

    colorRowList.append(borderColor + borderTextColor + "[ ]" + Style.RESET_ALL)
   
    return "".join(colorRowList)

def clear():
    """ Clears the screen. """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
      
      
def printBanner():
    """ Prints the banner, a 3D version of the word chess. """
    f = open('banner.txt', 'r')
    for line in f:
        colorLine = []
        stripLine = line.rstrip("\n")
        for i in stripLine:
            if i == "_":
                colorLine.append(Fore.BLUE+i+Style.RESET_ALL)
            else: 
                colorLine.append(Fore.RED+i+Style.RESET_ALL)
        
        print "".join(colorLine)
    i = raw_input("Press enter to start or \"?\" to view the rules!\n->")
    if "?" in i:
        printRules()
    
def printRules():
    """ Prints the rules of the game. """
    clear()
    f = open('rules.txt', 'r')
    for line in f:
        colorLine = []
        stripLine = line.rstrip("\n")
        for i in stripLine:
            if i == "_":
                colorLine.append(Fore.BLUE+i+Style.RESET_ALL)
            else: 
                colorLine.append(Fore.RED+i+Style.RESET_ALL)
        
        print "".join(colorLine)
    raw_input("\n\nPress enter to start/continue the game!\n->")
def main():
    """ The main program. """
    if name == 'nt':
        init()
    printBanner()
    board = Board()
    board.takeTurns()
if __name__ == "__main__":
        
    #sides=["TT","/\\","\/","||","()","!!","<>","><","\'\'"]  
    #mids=["v","b","!","#","^",".","_","-","|","?"]
    #for i in [s[0]+m+s[1] for m in mids for s in sides]:
    #    clear()
    #    raw_input(i)

    
    main()
