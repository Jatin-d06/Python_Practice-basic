# 2D list 
board = []

for i in range(8) : 
    row = ["Empty" for i in range(8)]
    board.append(row)

# for element in board : 
#     print(element)



board[0][0] = "rooks"
board[0][7] = "rooks"
board[7][0] = "rooks"
board[7][7] = "rooks"

for i in board:
    print([i])