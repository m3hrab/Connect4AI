import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (4, 102, 200)

# Set the dimensions of the screen
SCREEN_WIDTH = 930
SCREEN_HEIGHT = 630

class Button:
    def __init__(self, x, y, width, height, color, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 28)
        self.rendered_text = self.font.render(text, True, WHITE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_rect = self.rendered_text.get_rect(center=self.rect.center)
        surface.blit(self.rendered_text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True

class Help:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.Surface(screen.get_size())
        self.background.fill(WHITE)
        self.rules_text = [
            "Connect-4 is a two-player strategy game.",
            "The game is played on a vertical board with seven columns and six rows.",
            "Each player takes turns dropping a piece of their chosen color into a column.",
            "The piece falls to the lowest unoccupied slot in the column.",
            "The objective of the game is to connect four of one's own pieces of the same color",
            "vertically, horizontally, or diagonally before your opponent does.",
            "The first player to connect four pieces in a row wins the game.",
        ]
        self.rules_font = pygame.font.Font(None, 26)
        self.back_button = Button(SCREEN_WIDTH-120, SCREEN_HEIGHT - 50, 100, 40, BLUE, "Back")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif self.back_button.handle_event(event):
                    return

            # Draw the background and the rules text
            self.screen.blit(self.background, (0, 0))
            for i, line in enumerate(self.rules_text):
                text = self.rules_font.render(line, True, BLACK)
                text_rect = text.get_rect()
                text_rect.centerx = self.screen.get_rect().centerx
                text_rect.y = 50 + i * 30
                self.screen.blit(text, text_rect)

            # Draw the back button
            self.back_button.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
