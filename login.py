import pygame
import json
import sys 

class Login:
    def __init__(self, screen):
        self.screen = screen
        self.filename = "user_data.json"

        # set up input fields
        self.username = ""
        self.password = ""
        self.username_rect = pygame.Rect(300, 200, 200, 30)
        self.password_rect = pygame.Rect(300, 250, 200, 30)
        self.active_rect = None
        self.username_active = False
        self.password_active = False

        # set up buttons
        self.login_button = pygame.Rect(300, 300, 100, 30)
        self.back_button = pygame.Rect(450, 300, 100, 30)

        # load user data from file
        self.users = self.load_data()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_data()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.username_rect.collidepoint(event.pos):
                        self.username_active = True
                        self.password_active = False
                        self.active_rect = self.username_rect
                    elif self.password_rect.collidepoint(event.pos):
                        self.username_active = False
                        self.password_active = True
                        self.active_rect = self.password_rect
                    elif self.login_button.collidepoint(event.pos):
                        if self.check_login():
                            # login successful, return to menu
                            self.save_data()
                            # return
                            print("Login successfull")
                        else:
                            print("Login unsuccessfull")
                            
                    elif self.back_button.collidepoint(event.pos):
                        self.save_data()
                        return
                    else:
                        self.username_active = False
                        self.password_active = False
                        self.active_rect = None
                elif event.type == pygame.KEYDOWN:
                    if self.username_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.username = self.username[:-1]
                        else:
                            self.username += event.unicode
                    elif self.password_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.password = self.password[:-1]
                        else:
                            self.password += event.unicode

            self.screen.fill((255, 255, 255))

            # draw input fields
            pygame.draw.rect(self.screen, (0, 0, 0), self.username_rect, 2)
            pygame.draw.rect(self.screen, (0, 0, 0), self.password_rect, 2)
            if self.active_rect:
                pygame.draw.rect(self.screen, (255, 0, 0), self.active_rect, 2)
            font = pygame.font.SysFont('comicsansms', 25, True)
            username_text = font.render("Username:", True, (0, 0, 0))
            password_text = font.render("Password:", True, (0, 0, 0))
            self.screen.blit(username_text, (200, 200))
            self.screen.blit(password_text, (200, 250))
            username_input = font.render(self.username, True, (0, 0, 0))
            password_input = font.render("*" * len(self.password), True, (0, 0, 0))
            self.screen.blit(username_input, (self.username_rect.x + 5, self.username_rect.y + 5))
            self.screen.blit(password_input, (self.password_rect.x + 5, self.password_rect.y + 5))

            # draw
            # draw buttons
            pygame.draw.rect(self.screen, (0, 255, 0), self.login_button)
            pygame.draw.rect(self.screen, (0, 255, 0), self.back_button)
            login_text = font.render("Login", True, (255, 255, 255))
            back_text = font.render("Back", True, (255, 255, 255))
            self.screen.blit(login_text, (self.login_button.x + 10, self.login_button.y + 5))
            self.screen.blit(back_text, (self.back_button.x + 10, self.back_button.y + 5))

            pygame.display.flip()

    def check_login(self):
        # check if username and password match saved data
        print(self.username)
        print(self.password)
        print(self.users)
        for user in self.users:
            if self.username in user.keys() and self.password in user.values():
                return True
        return False

    def load_data(self):
        # load user data from file
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        return data

    def save_data(self):
        # save user data to file
        with open(self.filename, 'w') as f:
            json.dump(self.users, f)
