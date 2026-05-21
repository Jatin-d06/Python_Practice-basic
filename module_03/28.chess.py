# chess 

r = "rook"
p = "pawn "
kg = "king"
b = "bishop"
q = "queen"
k = "knight"


chess = [["  *  " for C in range(8) ] for R in range(8)]
for piece in chess: 
    print(piece)
print()
print()
print()
for R in range(8):
    for C in range(8):
        if R == 0 or R == 7 :
            if C == 0 or C == 7:
                chess[R][C] = r
        if R == 0 or R == 7 :
            if C == 1 or C == 6:
                chess[R][C] = k
        if R == 0 or R == 7 :
            if C == 2 or C == 5:
                chess[R][C] = b
        if R == 0 or R == 7 :
            if C == 4 :
                chess[R][C] = q
            if C == 3 :
                chess[R][C] = kg
        if R == 1:
            chess[R][C] = p
        if R == 6: 
            chess[R][C] = p 
for piece in chess: 
    print(piece)