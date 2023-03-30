import pygame
from borad import Board
from player import Player

class Game:

    def __init__(self, player1, player2):
    
        pygame.init()
        self.board = Board(6, 7)
        self.players = [Player(player1), Player(player2)]
        self.current_player = self.players[0]
        self.piece = 1
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
        # Draw the players name
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


        
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect-4")
        screen.fill((255, 255, 255))
        self.board.draw(screen)

        # Start the main loop for the game 
        while not self.game_over:
            
            # screen.fill((255, 255, 255))
            # self.board.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                    
                if event.type == self.timer_event:
                    if not self.timer_paused:
                        self.time_left -= 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # if event.key == pygame.K_SPACE:
                    #     self.timer_paused = not self.timer_paused
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

                if event.type == pygame.MOUSEBUTTONDOWN and not self.timer_paused: 
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

        winner_text = self.font2.render(f"Winner: {self.winner}", True, (0, 0, 0))
        screen.blit(winner_text, (40, 10))
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()
