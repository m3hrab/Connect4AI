import pygame
import json

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 930
SCREEN_HEIGHT = 630

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY =(222, 226, 230)
BLUE = (4, 102, 200)

# Set the font and font size
FONT = pygame.font.Font(None, 30)

# Load the user data from the JSON file
with open('user_data.json', 'r') as f:
    user_data = json.load(f)

# Define the signup screen function
def signup_screen(screen):
    # Clear the screen
    screen.fill(WHITE)

    text = "User Registration"
    # Set the title
    title = FONT.render(text, True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH/2, 100))
    screen.blit(title, title_rect)

    # Set the username label
    username_label = FONT.render("Username", True, BLACK)
    username_label_rect = username_label.get_rect(center=(SCREEN_WIDTH/2-140, 200))
    screen.blit(username_label, username_label_rect)

    # Set the password label
    password_label = FONT.render("Password", True, BLACK)
    password_label_rect = password_label.get_rect(center=(SCREEN_WIDTH/2-170, 250))
    screen.blit(password_label, password_label_rect)

    # Set the password label
    password_label = FONT.render("Confirm Password", True, BLACK)
    password_label_rect = password_label.get_rect(center=(SCREEN_WIDTH/2-170, 300))
    screen.blit(password_label, password_label_rect)

    # Create the username textbox
    username_textbox = pygame.Rect(SCREEN_WIDTH/2-50, 185, 250, 40)
    username = ""

    # Create the password textbox
    password_textbox = pygame.Rect(SCREEN_WIDTH/2-50, 235, 250, 40)
    password = ""

    # Create the confirm password textbox
    confirm_password_textbox = pygame.Rect(SCREEN_WIDTH/2-50, 285, 250, 40)
    confirm_password = ""

    # Create the Signup button
    signup_button = pygame.Rect(SCREEN_WIDTH/2-50, 350, 150, 40)
    signup_label = FONT.render("Signup", True, WHITE)
    signup_label_rect = signup_label.get_rect(center=signup_button.center)
    pygame.draw.rect(screen, BLUE, signup_button)
    screen.blit(signup_label, signup_label_rect)

    # Create the back button
    back_button = pygame.Rect(SCREEN_WIDTH/2-50, 420, 150, 40)
    back_label = FONT.render("Back", True, WHITE)
    back_label_rect = back_label.get_rect(center=back_button.center)
    pygame.draw.rect(screen, BLUE, back_button)
    screen.blit(back_label, back_label_rect)

    # Create the message box
    message_box = pygame.Rect(SCREEN_WIDTH/2-150, 500, 10, 50)

    # Update the display
    pygame.display.update()

    done = False
    # Main loop for the signup screen
    while not done:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if username_textbox.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                if password_textbox.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
                if confirm_password_textbox.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_BACKSPACE:
                        confirm_password = confirm_password[:-1]
                    else:
                        confirm_password += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the signup button was clicked
                if signup_button.collidepoint(event.pos):
                    # Check if the username is filed and passwords are match
                    if username != '' and password == confirm_password:
                        # Display the success message
                        user_data[username] = password
                        with open('user_data.json', 'w') as f:
                            json.dump(user_data, f)
                        success_message = FONT.render("Registratoin successful!", True, BLACK)
                        success_message_rect = success_message.get_rect(center=message_box.center)
                        pygame.draw.rect(screen, WHITE, message_box)
                        screen.blit(success_message, success_message_rect)
                        pygame.display.update()
                        username = ''
                        password = ''
                        confirm_password = ''
                        pygame.time.wait(1000)
                        return  
                    else:
                        # Display the error message
                        error_message = FONT.render("Password doesn't match", True, BLACK)
                        error_message_rect = error_message.get_rect(center=message_box.center)
                        pygame.draw.rect(screen, WHITE, message_box)
                        screen.blit(error_message, error_message_rect)
                        pygame.display.update()
                        
                # Check if the back button was clicked
                elif back_button.collidepoint(event.pos):
                    return 

        # Draw the username textbox
        pygame.draw.rect(screen, GRAY, username_textbox)
        username_surface = FONT.render(username, True, BLACK)
        username_rect = username_surface.get_rect(center=username_textbox.center)
        screen.blit(username_surface, username_rect)

        # Draw the password textbox
        pygame.draw.rect(screen, GRAY, password_textbox)
        password_surface = FONT.render("*" * len(password), True, BLACK)
        password_rect = password_surface.get_rect(center=password_textbox.center)
        screen.blit(password_surface, password_rect)

        # Draw the confirm password textbox
        pygame.draw.rect(screen, GRAY, confirm_password_textbox)
        confirm_password_surface = FONT.render("*" * len(confirm_password), True, BLACK)
        confirm_password_rect = confirm_password_surface.get_rect(center=confirm_password_textbox.center)
        screen.blit(confirm_password_surface, confirm_password_rect)

        # Update the display
        pygame.display.update()
    

