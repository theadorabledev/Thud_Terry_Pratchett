from Tkinter import *
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
        self.symbol = " D "
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
        self.symbol = " T "
        self.name = "Troll"
        self.points = 4
    def isValidMove(self, position, board):           
        """ Checks if the inputted position is a valid move. """        
        if position in board.boardDict:
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
        self.depth = 3
        self.count = 0
        self.currentPlayer = "Dwarf"
        self.edges = (
            ["ABCDE"[char]+str([11, 12, 13, 14, 15][num]) for char in range(len("ABCDE")) for num in range(char, len([1, 2, 3, 4, 5]))]+
            ["ABCDE"[char]+str([5, 4, 3, 2, 1][num]) for char in range(len("ABCDE")) for num in range(char, len([1, 2, 3, 4, 5]))]+
            ["ONMLK"[char]+str([5, 4, 3, 2, 1][num]) for char in range(len("ABCDE")) for num in range(char, len([1, 2, 3, 4, 5]))]+
            ["ONMLK"[char]+str([11, 12, 13, 14, 15][num]) for char in range(len("ABCDE")) for num in range(char, len([1, 2, 3, 4, 5]))]+["H8"]
        
        )   
        self.NoTheWorldMustBePeopled()
    def NoTheWorldMustBePeopled(self):#much ado about nothing -benedick
        """ Updates the player positions on the board. """
        self.boardDict = {}
        self.board = []
        self.boardGraphic=""
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
        
        #app.createWidgets()
        for pos in self.edges:
            self.changeCoordinateSign(pos, " X ")
    def getCoordinateSign(self, spot):
        """ Gets the coordinate sign of the inputted spot. """
        return self.board[15-int(spot[1:])][self.board[15].index("["+str(spot[0]).upper()+"]")]
    def changeCoordinateSign(self, spot, sign):
        """ Change the coordinate sign of the inputted spot. """
        self.board[15-int(spot[1:])][self.board[15].index("["+str(spot[0]).upper()+"]")] = sign


#class pieceButton(Button)

class Application(Frame):
    def pieceClicked(self,coord):
        if coord in self.board.boardDict.keys() and self.board.boardDict[coord].name == self.board.currentPlayer:
            if self.buttons[coord]["bg"] != "green":
                self.buttons[coord]["relief"] = "sunken"
                self.buttons[coord]["bg"] = "green"
                self.firstClick = False
                self.selectedPiece = coord
            else:
                self.buttons[coord]["relief"] = "raised"
                self.buttons[coord]["bg"] = self.buttonsLastColor[coord]
                self.firstClick = True
                self.selectedPiece = ""
        if not self.firstClick:
            if self.board.boardDict[self.selectedPiece].isValidMove(coord, self.board):
                self.board.boardDict[self.selectedPiece].movePiece(coord, self.board)
                if self.board.currentPlayer == "Dwarf":
                    self.board.currentPlayer = "Troll"
                else:
                    self.board.currentPlayer = "Dwarf"

                self.createWidgets()                                      
            
            
    def createWidgets(self):        
        self.buttons = {}
        self.buttonsLastColor = {}
        self.board.NoTheWorldMustBePeopled()
        for i in range(len(self.board.board)-1):
            b = Button(self, text=self.board.board[i][0],font='TkFixedFont')
            b.grid(row=i, column=1)             
            for j in range(1, len(self.board.board[i])):
                coord = "ABCDEFGHIJKLMNO"[j-1]+str(int(self.board.board[i][0][1:3]))
                b = Button(self, text= self.board.getCoordinateSign(coord) ,font='TkFixedFont', command=lambda coord=coord:self.pieceClicked(coord))
                #b.bind("<Enter>", self.pieceClicked)
                if coord in self.board.boardDict.keys() and self.board.boardDict[coord].name == "Dwarf":
                    b["fg"] = "red"
                if coord in self.board.boardDict.keys() and self.board.boardDict[coord].name == "Troll":
                    b["fg"] = "blue"
                blackCheckers=["ABCDEFGHIJKLMNO".index(coord[0]) % 2 != 0 and int(coord[1:]) % 2 == 0, "ABCDEFGHIJKLMNO".index(coord[0]) % 2 == 0 and int(coord[1:]) % 2 != 0]
                if any(blackCheckers) and not all(blackCheckers):
                    b["bg"] = "black"
                if self.board.getCoordinateSign(coord) == " X ":
                    b["bg"] = "red"
                    b["fg"] = "black"
                b.grid(row=i, column=j+1) 
                self.buttons[coord] = b
                self.buttonsLastColor[coord] = b["bg"]
        for i in range(len(self.board.board[-1])):
            b = Button(self, text=self.board.board[-1][i],font='TkFixedFont')
            b.grid(row=15, column=i+1)     
        self.playerTurnDisplay=Label(self, text= "Dwarf's turn!", font="TkFixedFont")
        self.playerTurnDisplay.pack()#grid(row=16)
        self.playerTurnDisplay.place(relx=.5, rely=1, anchor="center")

    def takeTurns(self):
        pass
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.buttons={}
        self.board=Board()
        self.createWidgets()
        self.firstClick=True
        self.selectedPiece=""


#board = Board()
root = Tk()
root.title= "Thud!"
        
#board.NoTheWorldMustBePeopled()
root.geometry="1600x1200"
app = Application(master=root)
app.mainloop()
root.destroy()
