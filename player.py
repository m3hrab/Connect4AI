import pygame

class Player:
    def __init__(self, name, game_piece_color):
        self.name = name
        self.game_piece_color = game_piece_color
    
    def make_move(self, board, column, piece):
        if board.is_valid_move(column):
            row = board.get_next_open_row(column)
            board.drop_piece(row, column, piece)
            # print(board)
            return True
        return False
