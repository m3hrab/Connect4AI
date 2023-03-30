import pygame
from borad import Board
from player import Player
import random
import numpy as np
import math

class HardGameAI:

    def __init__(self, player1, player2="AI"):
    
        pygame.init()
        self.board = Board(6, 7)
        self.players = [Player(player1), Player(player2)]
        temp = random.randint(0,1)
        self.current_player = self.players[temp]
        self.piece = temp+1
        self.empty = 0
        self.game_over = False
        self.winner = None
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.font2 = pygame.font.SysFont("comicsansms", 80)
        self.timer_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.timer_event, 1000)
        self.timer_paused = False
        self.time_left = 120
        self.width = 7 * 90 + 300 
        self.height = (6+1) * 90
        
    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
            self.piece = 2
        else:
            self.current_player = self.players[0]
            self.piece = 1
        self.time_left = 120

    def check_winner(self,screen):
        if self.board.get_winner():
            self.game_over = True
            self.board.draw(screen) #issues
            self.winner = self.current_player.name        
            return True
        elif self.board.is_full():
            self.game_over = True
            return True
        return False
    
    def draw_timer_button(self,screen):
        # Draw the button
        self.button_width = 180
        self.button_height = 60
        self.button_x = screen.get_rect().right - (self.button_width+40) 
        self.button_y = screen.get_rect().centery
        button_color = (0, 255, 0) if not self.timer_paused else (255, 0, 0)
        button_text = "Pause" if not self.timer_paused else "Resume"
        button_text_color = (255, 255, 255)
        button_text_pos = (self.button_x + self.button_width // 2, self.button_y + self.button_height // 2)
        button_text_surface = self.font.render(button_text, True, button_text_color)
        button_text_rect = button_text_surface.get_rect(center=button_text_pos)
        pygame.draw.rect(screen, button_color, (self.button_x, self.button_y, self.button_width, self.button_height))
        screen.blit(button_text_surface, button_text_rect)

    def draw_players(self,screen):
        # Draw the button
        width = 160
        height = 50
        x = screen.get_rect().right - (self.button_width+40) 
        y1 = screen.get_rect().centery - 180
        y2 = screen.get_rect().centery + 180
        text1 = self.players[0].name
        text2 = self.players[1].name 
        color_active = (255, 255, 255)
        color_pause = (50, 50, 50)
        text_pos1 = (x+width//2, y1+height//2)
        text_pos2 = (x+width//2, y2+height//2)
        if self.piece == 1:
            text_surface1 = self.font.render(text1, True, color_active)
            text_surface2 = self.font.render(text2, True, color_pause)
        else:
            text_surface1 = self.font.render(text1, True, color_pause)
            text_surface2 = self.font.render(text2, True, color_active)

        text_rect1 = text_surface1.get_rect(center=text_pos1)
        text_rect2 = text_surface2.get_rect(center=text_pos2)
        if self.piece == 1:
            pygame.draw.rect(screen, (69, 123, 157), (x, y1, width, height))
            pygame.draw.rect(screen, (229, 229, 229), (x, y2, width, height))
            pygame.draw.circle(screen, (24, 188, 156), (x-20, y1+25), 10)
            pygame.draw.circle(screen, (255, 255, 255), (x-20, y2+25), 10)
        else:
            pygame.draw.rect(screen, (229, 229, 229), (x, y1, width, height))
            pygame.draw.rect(screen, (69, 123, 157), (x, y2, width, height))
            pygame.draw.circle(screen, (44, 62, 80), (x-20, y2+25), 10)
            pygame.draw.circle(screen, (255, 255, 255), (x-20, y1+25), 10)


        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)

    # def evaluate_window(self, window):
        score = 0

        # checking AI players score 
        if window.count(2) == 4:
            score += 100
        elif window.count(2) == 3 and window.count(self.empty) == 1:
            score += 10
        elif window.count(2) == 2 and window.count(self.empty) == 2:
            score += 5 

        # checking for the oppent score    
        if window.count(1) == 3 and window.count(self.empty) == 1:
            score -= 80 

        return score 


    # def score_position(self, board):
        score = 0
        
        # score for center column
        center_array = [int(i) for i in list(board[:,3])]
        center_count = center_array.count(self.piece)
        score += center_count * 6
        
        # Score for horizontal
        for r in range(6): #row = 6
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(4): #col = 7-3 for 4 consicute piece
                window = row_array[c:c+4] #window length
                score += self.evaluate_window(window)

        # vertical score 
        for c in range(7): # Column = 7
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(6-3): #Row = 6
                window = col_array[r:r+4]
                score += self.evaluate_window(window)


        # Positive Sloped diagonal Scroe 
        for r in range(3): # row-3
            for c in range(4): # col-3
                window = [board[r+i][c+i] for i in range(4)]
                score += self.evaluate_window(window)


        # Negative sloped diagonal score 
        for r in range(3): # row-3
            for c in range(4): # col-3
                window = [board[r+3-i][c+i] for i in range(4)]
                score += self.evaluate_window(window)

        return score    
    
    # def is_terminal_node(self):
    #     return self.board.get_winner() or len(self.board.get_valid_moves()) == 0
    

    def evaluate_board(self):
        """
        Evaluates the current state of the game board and returns a score.
        """
        score = 0

        # Check horizontal scores
        for r in range(self.board.height):
            row_array = [int(i) for i in list(self.board.board[r,:])]
            for c in range(self.board.width - 3):
                window = row_array[c:c+4]
                score += self.evaluate_window(window)

        # Check vertical scores
        for c in range(self.board.width):
            col_array = [int(i) for i in list(self.board.board[:,c])]
            for r in range(self.board.height - 3):
                window = col_array[r:r+4]
                score += self.evaluate_window(window)

        # Check positively sloped diagonal scores
        for r in range(self.board.height - 3):
            for c in range(self.board.width - 3):
                window = [self.board.board[r+i][c+i] for i in range(4)]
                score += self.evaluate_window(window)

        # Check negatively sloped diagonal scores
        for r in range(self.board.height - 3):
            for c in range(self.board.width - 3):
                window = [self.board.board[r+3-i][c+i] for i in range(4)]
                score += self.evaluate_window(window)

        return score

    def minimax(self, depth, alpha, beta, maximizingPlayer):
        """
        Implementation of the Minimax algorithm with alpha-beta pruning.
        Returns the score of the best move for the current player at the current game state.
        """
        if self.game_over:
            if self.winner == self.players[0].name:
                return -1000000
            elif self.winner == self.players[1].name:
                return 1000000
            else:
                return 0

        if depth == 0:
            return self.evaluate_board()

        if maximizingPlayer:
            max_score = -np.inf
            for col in range(self.board.width):
                if self.board.is_valid_location(col):
                    self.board.drop_piece(col, self.piece)
                    score = self.minimax(depth - 1, alpha, beta, False)
                    self.board.remove_piece(col)
                    max_score = max(max_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            return max_score
        else:
            min_score = np.inf
            for col in range(self.board.width):
                if self.board.is_valid_location(col):
                    self.board.drop_piece(col, 3 - self.piece)
                    score = self.minimax(depth - 1, alpha, beta, True)
                    self.board.remove_piece(col)
                    min_score = min(min_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return min_score


    def pick_best_move(self):
        valid_moves = self.board.get_valid_moves()
        best_score = -10000 
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            row = self.board.get_next_open_row(col)
            temp_board = self.board.grid.copy()
            temp_board[row][col] = self.piece
            score = self.score_position(temp_board)
            if score > best_score:
                best_score = score
                best_col = col
        
        return best_col

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect-4")
        screen.fill((255, 255, 255))
        self.board.draw(screen)

        # Start the main loop for the game 
        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                    
                if event.type == self.timer_event:
                    if not self.timer_paused:
                        self.time_left -= 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_x <= mouse_pos[0] <= self.button_x + self.button_width and \
                            self.button_y <= mouse_pos[1] <= self.button_y + self.button_height:
                        # Pause/resume the timer
                        self.timer_paused = not self.timer_paused

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if (mouse_pos[0] >= 20 and mouse_pos[0] <= (int(6*90+90/2) + 40)):
                        pygame.draw.rect(screen, (255,255,255), (0,0, 930, 90))
                        posx = event.pos[0]
                        if (posx >= 0 and posx <= (int(6*90+90/2) + 20)) and (self.piece%2)==1:
                            pygame.draw.circle(screen, (24, 188, 156), (posx+30, int(90/2)), 30)
                        elif (posx >= 0 and posx <= (int(6*90+90/2) + 20)) and (self.piece%2)==0:
                            pygame.draw.circle(screen, (44, 62, 80), (posx+30, int(90/2)), 30)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN and not self.timer_paused and self.current_player == self.players[0]: 
                    mouse_pos = pygame.mouse.get_pos()
                    if (mouse_pos[0] >= 20 and mouse_pos[0] <= (int(6*90+90/2) + 40)):
                        column = mouse_pos[0]//90
                        pygame.draw.rect(screen, (255,255,255), (0,0, 930, 90))
                        if self.current_player.make_move(self.board, column, self.piece):
                            if self.check_winner(screen):
                                break
                            self.switch_player()
            
            timer_text = self.font.render(f"Time Left: {self.time_left} seconds", True, (0, 0, 0))
            # Remove Previous drawn screen
            pygame.draw.rect(screen, (255,255,255), (680,280, 300, 100))
            screen.blit(timer_text, (680, 280))  
            self.draw_timer_button(screen)
            self.draw_players(screen)
            self.board.draw(screen)
            pygame.display.update()
            # self.clock.tick(60)

            # AI Turns
            if (self.current_player==self.players[1]):
                column = self.pick_best_move()
                pygame.time.wait(random.randint(500,1000))
                pygame.draw.rect(screen, (255,255,255), (0,0, 930, 90))
                if self.current_player.make_move(self.board, column, self.piece):
                    if self.check_winner(screen):
                        break
                    self.switch_player()


        winner_text = self.font2.render(f"Winner: {self.winner}", True, (0, 0, 0))
        screen.blit(winner_text, (40, 10))
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()
