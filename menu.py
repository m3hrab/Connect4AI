import pygame
from game import Game

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the window size
WINDOW_SIZE = (930, 630)

# Define the font for the menu buttons
BUTTON_FONT = pygame.font.Font(None, 40)

# Create a class for the menu buttons
class Button:
    def __init__(self, x, y, width, height, text, function):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.function = function

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect)
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
def play():
    Game("Mehrab", "Joti").run()

def leaderboard():
    print("Leaderboard")

def player1_login():
    print("Player 1 Login")

def player2_login():
    print("Player 2 Login")

# Create the menu screen and add the buttons
screen = pygame.display.set_mode(WINDOW_SIZE)
menu = Menu(screen)
menu.add_button(200, 100, 400, 50, "Play", play)
menu.add_button(200, 200, 400, 50, "Leaderboard", leaderboard)
menu.add_button(200, 300, 400, 50, "Player 1 Login", player1_login)
menu.add_button(200, 400, 400, 50, "Player 2 Login", player2_login)

# Run the menu screen
menu.run()

# Quit Pygame
pygame.quit()
