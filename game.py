from pprint import pprint

gMap = [[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,'X','X',0,0,'X','X',0,0],
       [0,0,'X','X',0,0,'X','X',0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]
       ]



class Piece():
    iden = 0
    def __init__(self, n, o=True): #n=value of piece, o=owned (True of False)
        self.num = n #Spy = 1, Bomb = 12, Flag = 13
        self.owned = o
        self.id = Piece.iden
        Piece.iden += 1
    x = -1
    y = -1
    
    def move(self, drn, dst=1): #may not use
        print("Move " + str(drn) + " " + str(dst))

    def place(self, xPos, yPos):
        self.x = xPos
        self.y = yPos


def placePiece(m, p, x, y):
    if(m[y][x] == 0):
        p.place(x, y);
        m[y][x] = p
    else:
        print("Can't place piece there!")

def movePiece(m, p, x, y):
    if(p.num == 2):
        #add functionality for 2 piece to move full board
        print("Wait for feature")
    else: #change to elif that checks that piece is an enemy piece
        if(m[y][x] == 'X'):
            print("Can't move piece there!")
        elif(isinstance(m[y][x], Piece)):
            if(m[y][x].num > p.num):
                m[p.y][p.x] = 0;
                p.place(-1,-1)
                print("Attacker killed")
            elif(m[y][x].num == p.num):
                m[p.y][p.x] = 0;
                m[y][x] = 0;
                p.place(-1,-1);
                print("Both pieces killed")
                 
            else:
                m[p.y][p.x] = 0;
                p.place(x, y);
                m[y][x] = p # Doesn't actually kill piece (piece stilll thinks its there)
                print("Defender killed") #Add feature to actually kill piece
        else:
            m[p.y][p.x] = 0;
            p.place(x, y);
            m[y][x] = p
            
def printMap(m):
    for i in range(len(m)):
        line = ''
        for y in range(len(m[i])):
            if(isinstance(m[i][y], Piece)): #add check for player ownership (don't display num if enemy piece)
                line += str(m[i][y].num)
            else:
                line += str(m[i][y])
        print line

     
