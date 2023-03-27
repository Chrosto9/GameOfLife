def init(widht: int, height: int) -> list:
    """
    Creates a 2D list of zeros with the given widht and height
    """
    board = []

    for x in range(HEIGHT):
        row = []
        for y in range(WIDHT):
            row.append(0)
        board.append(row)
    
    return board

def display(board: list):
    for row in board:
        print(row)
