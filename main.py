WIDHT = 10
HEIGHT = 10

board = []
for x in range(HEIGHT):
    row = []
    for y in range(WIDHT):

        row.append(0)

    board.append(row)
    
def display(board):
    for row in board:
        print(row)

display(board)
