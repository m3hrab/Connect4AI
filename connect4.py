# import numpy as np

# ROW_COUNT = 6
# COL_COUNT = 7
# def create_board():
#     board = np.zeros((ROW_COUNT, COL_COUNT))
#     return board 

# def drop_piece(board, row, col, piece):
#     board[row][col] = piece

# def is_valid_location(board, col):
#     return board[5][col] == 0

# def get_next_open_row(board, col):
#     for row in range(ROW_COUNT):
#         if board[row][col] == 0:
#             return row 

# def print_board(board):
#     print(np.flip(board,0))

# board = create_board()
# print(board)
# game_over = False 
# turn = 0

# while not game_over:
#     # Asks for player 1 inputs
#     if turn == 0:
#         col = int(input("Player 1 Make you Selection(0-6): "))

#         if is_valid_location(board, col):
#             row = get_next_open_row(board, col)
#             drop_piece(board, row, col, 1)

#     # Asks for Player 2 inputes
#     else:
#         col = int(input("Player 2 make you Selection(0-6): "))
        
#         if is_valid_location(board, col):
#             row = get_next_open_row(board, col)
#             drop_piece(board, row, col, 2)

#     print_board(board)
#     turn += 1
#     turn = turn % 2