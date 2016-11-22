from game import *


pieces = []

flag = Piece(13)
pieces.append(flag)

for i in range(6):
    b = Piece(12)
    pieces.append(b)

spy = Piece(1)
pieces.append(spy)


for s in range(8):
    s = Piece(2)
    pieces.append(s)

for m in range(5):
    m = Piece(3)
    pieces.append(m)

for s in range(4):
    s = Piece(4)
    pieces.append(s)

for s in range(4):
    s = Piece(5)
    pieces.append(s)

for s in range(4):
    s = Piece(6)
    pieces.append(s)

for s in range(3):
    s = Piece(7)
    pieces.append(s)

for s in range(2):
    s = Piece(8)
    pieces.append(s)

General = Piece(9)
pieces.append(General)

Marshall = Piece(10)
pieces.append(Marshall)
