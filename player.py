class Player:
    def __init__(self, name):
        self.name = name
    
    def make_move(self, board, column, piece):
        # Check the valid moves and update the player pieces 
        if board.is_valid_move(column):
            row = board.get_next_empty_row(column)
            board.drop_piece(row, column, piece)
            # print(board)
            return True
        return False
