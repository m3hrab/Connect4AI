import pygame
from game import Game
from login import Login
from easy_ai_player import EasyGameAI
from medium_ai_player import Game
# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (4, 102, 200)
GRAY = (222, 226, 230)

# Define the window size
WINDOW_SIZE = (930, 630)

# Define the font for the menu buttons
BUTTON_FONT = pygame.font.Font(None, 30)

# Create a class for the menu buttons
class Button:
    def __init__(self, x, y, width, height, text, function):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.function = function

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)
        text_surface = BUTTON_FONT.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.function()

# Create a class for the menu screen
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.running = True

    def add_button(self, x, y, width, height, text, function):
        button = Button(x, y, width, height, text, function)
        self.buttons.append(button)

    def draw(self):
        self.screen.fill(WHITE)
        # Game Title
        # title_font = pygame.font.Font(None, 80)
        title_font = pygame.font.SysFont('comicsansms', 100, True)
        title_text = title_font.render("Connect-4", True, BLUE)
        title_rect = title_text.get_rect()
        title_rect.centerx = self.screen.get_rect().centerx
        title_rect.centery = 100
        self.screen.blit(title_text, title_rect)
        pygame.draw.rect(screen, GRAY, (rect.left+30, rect.centery-20, 200, 300))
        pygame.draw.rect(screen, GRAY, (rect.right-230, rect.centery-20, 200, 300))
        pygame.draw.rect(screen, GRAY, (rect.centerx-200, rect.centery-20, 400, 300))
        for button in self.buttons:
            button.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for button in self.buttons:
                button.handle_event(event)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

# Define the functions to be called when the menu buttons are clicked
def multiplayer():
    Game("Mehrab", "Joti").run()

def easy_ai():
    EasyGameAI("Mehrab").run()

def leaderboard():
    print("Leaderboard")

def player1_login():
    # Define the window size
    WINDOW_SIZE = (930, 630)    
    screen = pygame.display.set_mode(WINDOW_SIZE)
    Login(screen).run()

def player2_login():
    print("Player 2 Login")

def help():
    print("help")

# Create the menu screen and add the buttons
screen = pygame.display.set_mode(WINDOW_SIZE)
rect = screen.get_rect()

# Draw the table rects
menu = Menu(screen)
menu.add_button(rect.centerx-100, rect.centery-80, 200, 40, "Leaderboard", leaderboard)
menu.add_button(rect.centerx-140, rect.centery+60, 130, 40, "Easy", easy_ai)
menu.add_button(rect.centerx+10, rect.centery+60, 130, 40, "Meduim", multiplayer)
menu.add_button(rect.centerx-140, rect.centery+110, 130, 40, "Hard", multiplayer)
menu.add_button(rect.centerx+10, rect.centery+110, 130, 40, "2 Player", multiplayer)
menu.add_button(rect.left+30, rect.centery-80, 200, 40, "Player 1 Login", player1_login)
menu.add_button(rect.right-230, rect.centery-80, 200, 40, "Player 2 Login", player2_login)
menu.add_button(rect.top+10, rect.left+10, 80, 40, "Help", player2_login)




# Run the menu screen
menu.run()

# Quit Pygame
pygame.quit()
