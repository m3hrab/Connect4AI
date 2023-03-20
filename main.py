import numpy as np 

ROW_COUNTS = 6
COLUMN_COUNTS = 7
def create_board():
    board = np.zeros((ROW_COUNTS, COLUMN_COUNTS))
    return board 

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for row in range(ROW_COUNTS):
        if board[row][col] == 0:
            return row
        
def print_board(board):
    print(np.flip(board,0))


def wining_move(board, piece):
    # horizontal locations 
    for c in range(COLUMN_COUNTS-3):
        for r in range(ROW_COUNTS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3]== piece:
                return True
            
    
    # vartical locations
    for c in range(COLUMN_COUNTS):
        for r in range(ROW_COUNTS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c]== piece:
                return True
            
    # checked positively slope diagonal
    for c in range(COLUMN_COUNTS-3):
        for r in range(ROW_COUNTS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3]== piece:
                return True
            
    # checked negatively slope diagonal


board = create_board()
print(board)

game_over = False
turn = 0
# main game loop 
while not game_over:

    # Ask for the player 1 turn 
    if turn == 0:
        col = int(input("Player 1 make your selection(0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if wining_move(board, 1):
                print("**Congrats**\nPlayer 1 wins")
                game_over = True

    # Ask for the player 2 turn 
    else:
        col = int(input("Player 2 make your selection(0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if wining_move(board, 2):
                print("**Congrats**\nPlayer 2 wins")
                game_over = True

    print_board(board)
    turn += 1
    turn = turn % 2

