import pygame
import sys
import numpy as np
import math

# Initializing pygame
pygame.init()

# Defines colors 
BOARD_COLOR = (222, 226, 230)
WHITE = (255,255,255)
PLAYER_1_COLOR = (24, 188, 156)
PLAYER_2_COLOR = (44, 62, 80)

def create_board():
	# creates a 2D array that represents the game board
	board = np.zeros((ROW,COLUMN))
	return board

def is_valid_move(board, col):
	# checks whether a given move is valid or not 
	# by verifying if the chosen column is not full.
	return board[ROW-1][col] == 0

def drop_piece(board, row, col, piece):
	# places a game piece (e.g., a colored disc) in the lowest 
	# available row of the selected column on the game board, and updates the board accordingly.
	board[row][col] = piece

def get_next_empty_row(board, col):
	# returns the index of the lowest empty row in the selected column
	for r in range(ROW):
		if board[r][col] == 0:
			return r

def print_board(board):
	# display the grid 
	print(board)
	# print(np.flip(board, 0))

def winning_move(board, piece):
	"""
	checks if a given move has resulted in a player
	winning the game by connecting four game pieces of the same color 
	vertically, horizontally, or diagonally.
	"""

	# Check horizontal locations for win
	for c in range(COLUMN-3):
		for r in range(ROW):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN):
		for r in range(ROW-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN-3):
		for r in range(ROW-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN-3):
		for r in range(3, ROW):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board(board):
	"""
	Draws the current state of the game board, including any game pieces that
	have been placed on it, in a graphical user interface, making it visually appealing and easier for players to interact with the game.
	"""
	for c in range(COLUMN):
		for r in range(ROW):
			pygame.draw.rect(screen, BOARD_COLOR, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN):
		for r in range(ROW):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, PLAYER_1_COLOR, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, PLAYER_2_COLOR, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()


ROW = 6
COLUMN = 7
SQUARESIZE = 90
RADIUS = int(SQUARESIZE/2 - 10)
width = COLUMN * SQUARESIZE
height = (ROW+1) * SQUARESIZE

game_over = False
turn = 0

# Create a 2D array to represent the board
board = create_board()

# Sets up the Pygame display window
screen = pygame.display.set_mode((width, height))

# fill the screen with white background color
screen.fill(WHITE)

draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

# Start the main game loop 
while not game_over:

	# Checks for the keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, WHITE, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, PLAYER_1_COLOR, (posx, int(SQUARESIZE/2)), RADIUS)
			else: 
				pygame.draw.circle(screen, PLAYER_2_COLOR, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		# looking for mouse button click event
		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, WHITE, (0,0, width, SQUARESIZE))

			# Ask for player 1 Input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_move(board, col):
					row = get_next_empty_row(board, col)
					drop_piece(board, row, col, 1)

					if winning_move(board, 1):
						label = myfont.render("Winner: Player-1", 1, PLAYER_1_COLOR)
						screen.blit(label, (40,10))
						game_over = True


			# Ask for Player 2 Input
			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_move(board, col):
					row = get_next_empty_row(board, col)
					drop_piece(board, row, col, 2)

					if winning_move(board, 2):
						label = myfont.render("Winner: Player - 2", 1, PLAYER_2_COLOR)
						screen.blit(label, (40,10))
						game_over = True

			# Display the updated board
			draw_board(board)

			turn += 1
			# Change the palyers turn
			turn = turn % 2

			if game_over:
				pygame.time.wait(5000)