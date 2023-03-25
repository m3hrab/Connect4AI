import pygame
from borad import Board
from player import Player

class Game:

    def __init__(self, player1, player2):
    
        pygame.init()
        self.board = Board(6, 7)
        self.players = [Player(player1, (255, 0, 0)), Player(player2, (255, 255, 0))]
        self.current_player = self.players[0]
        self.piece = 1
        self.game_over = False
        self.winner = None
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
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

                    
                # elif event.type == self.timer_event:
                #     if not self.timer_paused:
                #         self.time_left -= 1
                # elif event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_SPACE:
                #         self.timer_paused = not self.timer_paused
                # elif event.type == pygame.MOUSEBUTTONDOWN and not self.timer_paused:

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

                if event.type == pygame.MOUSEBUTTONDOWN: # and not self.timer_paused:
                    # column = event.pos[0] // 90
                    mouse_pos = pygame.mouse.get_pos()
                    if (mouse_pos[0] >= 20 and mouse_pos[0] <= (int(6*90+90/2) + 40)):
                        column = mouse_pos[0]//90
                        pygame.draw.rect(screen, (255,255,255), (0,0, 930, 90))
                        if self.current_player.make_move(self.board, column, self.piece):
                            if self.check_winner(screen):
                                break
                            self.switch_player()

            # timer_text = self.font.render(f"Time Left: {self.time_left}", True, (0, 0, 0))
            # screen.blit(timer_text, (10, 10))
            self.board.draw(screen)
            pygame.display.update()
            # self.clock.tick(60)

        # winner_text = self.font.render(f"Winner: {self.winner}", True, (255, 255, 255))
        # screen.blit(winner_text, (250, 10))
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()

Game("Mehrab", "Joti").run()