import pygame
import numpy as np

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cell_size = 90 
        self.radius = 30
        self.grid = np.zeros((6,7))
    
    def draw(self, screen):
        # Draw the board 
        for c in range(7):
            for r in range(6):
                pygame.draw.rect(screen, (222, 226, 230), (c*self.cell_size + 20, r*self.cell_size+self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.circle(screen, (255,255,255), (int(c*self.cell_size+self.cell_size/2) + 20, int(r*self.cell_size+self.cell_size+self.cell_size/2)), self.radius)
        
        # Draw the game pieces
        for c in range(7):
            for r in range(6):
                if self.grid[r][c] == 1:
                    pygame.draw.circle(screen, (24, 188, 156), (int(c*self.cell_size+self.cell_size/2) + 20 , 630-int(r*self.cell_size+self.cell_size/2)), self.radius)
                elif self.grid[r][c] == 2:
                    pygame.draw.circle(screen, (44, 62, 80), (int(c*self.cell_size+self.cell_size/2) + 20, 630-int(r*self.cell_size+self.cell_size/2)), self.radius)
    
    def is_valid_move(self, column):
        return self.grid[5][column] == 0
    
    def drop_piece(self, row, column, piece):
        self.grid[row][column] = piece
        # print(np.flip(self.grid,0))
            
    def get_next_open_row(self, col):
        # find the next open window to drop piece 
        for r in range(6):
            if self.grid[r][col] == 0:
                return r

    def get_winner(self):
        # Check rows for winner
        for i in range(self.rows):
            for j in range(self.columns - 3):
                if self.grid[i][j] == self.grid[i][j+1] == self.grid[i][j+2] == self.grid[i][j+3] != 0:
                    # return self.grid[i][j]
                    return True

        # Check columns for winner
        for i in range(self.rows - 3):
            for j in range(self.columns):
                if self.grid[i][j] == self.grid[i+1][j] == self.grid[i+2][j] == self.grid[i+3][j] != 0:
                    # return self.grid[i][j]
                    return True

        # Check diagonals for winner
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

        # Check full
    def is_full(self):
        for i in range(6):
            for j in range(7):
                if self.grid[i][j] == 0:
                    return False
        return True

    def reset(self):
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def get_valid_moves(self):
        valid_moves = []
        for i in range(self.columns):
            if self.is_valid_move(i):
                valid_moves.append(i)
        return valid_moves

    def __str__(self):
        return str(self.grid)
    
