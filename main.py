import pygame
import sys
import numpy as np
import math
import time 

# Global variables 
# colors 
GRAY = (222, 226, 230)
WHITE = (255,255,255)
BLACK = (0,0,0)
P1_COLOR = (24, 188, 156)
P2_COLOR = (44, 62, 80)

# define rows and columns 
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	# generate 6X7 arrays to represent the connect-4 board 
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	# Drop the piece based on selected columns
	board[row][col] = piece

def is_valid_location(board, col):
	# check the valid location for drop piece 
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
	# find the next open window to drop piece 
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

# def print_board(board):
# 	print(np.flip(board, 0))

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board(board):
	"Draw the board into pygame window"
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, GRAY, (c*SQUARESIZE + 20, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2) + 20, int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, P1_COLOR, (int(c*SQUARESIZE+SQUARESIZE/2) + 20 , height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, P2_COLOR, (int(c*SQUARESIZE+SQUARESIZE/2) + 20, height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	# pygame.display.update()


pygame.init()
board = create_board()
game_over = False
turn = 0
SQUARESIZE = 90

width = COLUMN_COUNT * SQUARESIZE + 300
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)
RADIUS = int(SQUARESIZE/2 - 12)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect-4")
screen.fill(WHITE)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont('comicsansms', 60)
font = pygame.font.SysFont("comicsansms", 30)

# Set the button size and position
button_width = 180
button_height = 60
button_x = screen.get_rect().right - (button_width+40) 
button_y = screen.get_rect().centery

# Set the initial time and timer state
start_time = time.time()
elapsed_time = 0
timer_paused = False

# Set the countdown timer duration
countdown_duration = 2 * 60  # 2 minutes in seconds


# start the main loop for the game 
while not game_over:

    # start the event loop 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, WHITE, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if (posx >= 0 and posx <= (int(6*SQUARESIZE+SQUARESIZE/2) + 20)) and turn==0:
				pygame.draw.circle(screen, P1_COLOR, (posx+30, int(SQUARESIZE/2)), RADIUS)
			elif (posx >= 0 and posx <= (int(6*SQUARESIZE+SQUARESIZE/2) + 20)) and turn==1:
				pygame.draw.circle(screen, P2_COLOR, (posx+30, int(SQUARESIZE/2)), RADIUS)

		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if (mouse_pos[0] >= 0 and mouse_pos[0] <= (int(6*SQUARESIZE+SQUARESIZE/2) + 20)):
				pygame.draw.rect(screen, WHITE, (0,0, width, SQUARESIZE))
				if turn == 0:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))

					if is_valid_location(board, col):
						# check the valid location to drop the piece 
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 1)

						if winning_move(board, 1):
							# check the winning_move 
							label = myfont.render("Player 1 win", 1, P1_COLOR)
							screen.blit(label, (40,10))
							game_over = True


				# # Ask for Player 2 Input
				else:				
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))

					if is_valid_location(board, col):
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 2)

						if winning_move(board, 2):
							label = myfont.render("Player 2 win", 1, P2_COLOR)
							screen.blit(label, (40,10))
							game_over = True


			if button_x <= mouse_pos[0] <= button_x + button_width and \
                    button_y <= mouse_pos[1] <= button_y + button_height:
				# Pause/resume the timer
				timer_paused = not timer_paused

			# print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2

			# Draw the button
			button_color = (0, 255, 0) if not timer_paused else (255, 0, 0)
			button_text = "Pause" if not timer_paused else "Resume"
			button_text_color = (255, 255, 255)
			button_text_pos = (button_x + button_width // 2, button_y + button_height // 2)
			button_text_surface = font.render(button_text, True, button_text_color)
			button_text_rect = button_text_surface.get_rect(center=button_text_pos)
			pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
			screen.blit(button_text_surface, button_text_rect)

			# Draw the countdown timer
			if not timer_paused:
				elapsed_time = time.time() - start_time
				remaining_time = countdown_duration - elapsed_time
				if remaining_time < 0:
					remaining_time = 0
					timer_paused = True
				remaining_minutes = int(remaining_time // 60)
				remaining_seconds = int(remaining_time % 60)
				timer_text = font.render(f"{remaining_minutes:02d}:{remaining_seconds:02d}", True, (0, 0, 0))
			else:
				timer_text = font.render(f"{remaining_minutes:02d}:{remaining_seconds:02d}", True, (128, 128, 128))
			screen.blit(timer_text, (width // 2 - timer_text.get_width() + 370, button_y - timer_text.get_height() - 10))

			pygame.display.flip()


	if game_over:
		# just for hold the screen ;)
		a = int(input())