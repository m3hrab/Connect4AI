import pygame
import numpy as np

class Board:
    """
    This class represents the Board for connect - 4
    """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cell_size = 90 
        self.radius = 30

        # Defines colors 
        self.board_color = (222, 226, 230)
        self.color_white = (255,255,255)
        self.p1_color = (24, 188, 156)
        self.p2_color = (44, 62, 80)

    	# creates a 2D array that represents the game board
        self.grid = np.zeros((self.rows, self.columns))
    
    def draw(self, screen):

        # Draw the main board 
        for c in range(7):
            for r in range(6):
                pygame.draw.rect(screen, self.board_color, (c*self.cell_size + 20, r*self.cell_size+self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.circle(screen, self.color_white, (int(c*self.cell_size+self.cell_size/2) + 20, int(r*self.cell_size+self.cell_size+self.cell_size/2)), self.radius)
        
        # Draw the game pieces
        for c in range(7):
            for r in range(6):
                if self.grid[r][c] == 1:
                    pygame.draw.circle(screen, self.p1_color, (int(c*self.cell_size+self.cell_size/2) + 20 , 630-int(r*self.cell_size+self.cell_size/2)), self.radius)
                elif self.grid[r][c] == 2:
                    pygame.draw.circle(screen, self.p2_color, (int(c*self.cell_size+self.cell_size/2) + 20, 630-int(r*self.cell_size+self.cell_size/2)), self.radius)
    
    def is_valid_move(self, column):
	    # checks whether a given move is valid or not 
        return self.grid[5][column] == 0
    
    def drop_piece(self, row, column, piece):
        # places a game piece (e.g., a colored disc) in the lowest 
        self.grid[row][column] = piece
            
    def get_next_empty_row(self, col):
	    # returns the index of the lowest empty row in the selected column
        for r in range(6):
            if self.grid[r][col] == 0:
                return r

    def get_winner(self):
        """
        checks if a given move has resulted in a player
        winning the game by connecting four game pieces of the same color 
        vertically, horizontally, or diagonally.
        """

        # Check horizontally 
        for i in range(self.rows):
            for j in range(self.columns - 3):
                if self.grid[i][j] == self.grid[i][j+1] == self.grid[i][j+2] == self.grid[i][j+3] != 0:
                    # return self.grid[i][j]
                    return True

        # Check  vertically
        for i in range(self.rows - 3):
            for j in range(self.columns):
                if self.grid[i][j] == self.grid[i+1][j] == self.grid[i+2][j] == self.grid[i+3][j] != 0:
                    # return self.grid[i][j]
                    return True

        # Check diagonally
        for i in range(self.rows - 3):
            for j in range(self.columns - 3):
                if self.grid[i][j] == self.grid[i+1][j+1] == self.grid[i+2][j+2] == self.grid[i+3][j+3] != 0:
                    # return self.grid[i][j]
                    return True

        for i in range(3, self.rows):
            for j in range(self.columns - 3):
                if self.grid[i][j] == self.grid[i-1][j+1] == self.grid[i-2][j+2] == self.grid[i-3][j+3] != 0:
                    # return self.grid[i][j]
                    return True

        
    def is_full(self):
        # retrun the board is full or not
        for i in range(6):
            for j in range(7):
                if self.grid[i][j] == 0:
                    return False
        return True

    def reset(self):
        # reset the game board
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def get_valid_moves(self):
        valid_moves = []
        for i in range(self.columns):
            if self.is_valid_move(i):
                valid_moves.append(i)
        return valid_moves
    
