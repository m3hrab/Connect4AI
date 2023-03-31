import pygame
from game import Game
from easy_ai_player import EasyGameAI
from medium_ai_player import MediumGameAI
from hard_ai_player import HardGameAI
import login
import signup 
from help import Help

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (4, 102, 200)
GRAY = (222, 226, 230)
RED = (240, 20, 20)
COLOR1 = (24, 188, 156)
COLOR2 = (44, 62, 80)

# Define the window size
WINDOW_SIZE = (930, 630)
user1 = ''
user2 = ''
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
        if user1 != '':
            font = pygame.font.Font(None, 30)
            username = font.render(user1, True, COLOR1)
            username_rect = (rect.left+80, rect.centery+20)
            screen.blit(username, username_rect)
        pygame.draw.rect(screen, GRAY, (rect.right-230, rect.centery-20, 200, 300))
        if user2 != '':
            font = pygame.font.Font(None, 30)
            username2 = font.render(user2, True, COLOR2)
            username2_rect = (rect.right-200, rect.centery)
            screen.blit(username2, username2_rect)
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

# Create the menu screen and add the buttons
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Connect-4")
rect = screen.get_rect()
# Define the functions to be called when the menu buttons are clicked
def multiplayer():
    if user1 !='' and user2 != '':
        Game(user1, user2).run()
    else:
        # pygame.draw.rect(screen, GRAY, (rect.centerx-140, rect.centery+140, 300, 200))
        font = pygame.font.Font(None, 30)
        msg = font.render("Please Login First", True, RED)
        msg_rect = (rect.centerx-80, rect.centery)
        screen.blit(msg, msg_rect)
        pygame.display.update()
        pygame.time.wait(1000)

def easy_ai():
    if user1 != '':
        EasyGameAI(user1).run()
    elif user2 != '':
        EasyGameAI(user2).run()
    else:
        font = pygame.font.Font(None, 30)
        msg = font.render("Please Login First", True, RED)
        msg_rect = (rect.centerx-80, rect.centery)
        screen.blit(msg, msg_rect)
        pygame.display.update()
        pygame.time.wait(1000)

def medium_ai():
    if user1 != '':
            MediumGameAI(user1).run()
    elif user2 != '':
        MediumGameAI(user2).run()
    else:
        font = pygame.font.Font(None, 30)
        msg = font.render("Please Login First", True, RED)
        msg_rect = (rect.centerx-80, rect.centery)
        screen.blit(msg, msg_rect)
        pygame.display.update()
        pygame.time.wait(1000)

def hard_ai():
    if user1 != '':
            MediumGameAI(user1).run()
    elif user2 != '':
        MediumGameAI(user2).run()
    else:
        font = pygame.font.Font(None, 30)
        msg = font.render("Please Login First", True, RED)
        msg_rect = (rect.centerx-80, rect.centery)
        screen.blit(msg, msg_rect)
        pygame.display.update()
        pygame.time.wait(1000)

def player1_login():
    global user1
    user1 = login.login_screen(screen, 1)

def player2_login():
    global user2
    user2 = login.login_screen(screen, 2)
def help():
    Help(screen).run()

def create_account():
    signup.signup_screen(screen)

# Draw the table rects
menu = Menu(screen)
menu.add_button(rect.centerx-100, rect.centery-80, 200, 40, "Create Account", create_account)
menu.add_button(rect.centerx-140, rect.centery+60, 130, 40, "Easy", easy_ai)
menu.add_button(rect.centerx+10, rect.centery+60, 130, 40, "Meduim", medium_ai)
menu.add_button(rect.centerx-140, rect.centery+110, 130, 40, "Hard", medium_ai)
menu.add_button(rect.centerx+10, rect.centery+110, 130, 40, "2 Player", multiplayer)
menu.add_button(rect.left+30, rect.centery-80, 200, 40, "Player 1 Login", player1_login)
menu.add_button(rect.right-230, rect.centery-80, 200, 40, "Player 2 Login", player2_login)
menu.add_button(rect.top+10, rect.left+10, 80, 40, "Help", help)
# menu.add_button()


# Run the menu screen
menu.run()

# Quit Pygame
pygame.quit()
