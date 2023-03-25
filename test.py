import pygame
import time

pygame.init()

# Set the width and height of the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the font and font size
font = pygame.font.SysFont("comicsansms", 40)

# Set the button size and position
button_width = 180
button_height = 60
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2

# Set the initial time and timer state
start_time = time.time()
elapsed_time = 0
timer_paused = False

# Set the countdown timer duration
countdown_duration = 2 * 60  # 2 minutes in seconds

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Check if the mouse button is pressed over the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_x <= mouse_pos[0] <= button_x + button_width and \
                    button_y <= mouse_pos[1] <= button_y + button_height:
                # Pause/resume the timer
                timer_paused = not timer_paused

    screen.fill((255, 255, 255))

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
    screen.blit(timer_text, (screen_width // 2 - timer_text.get_width() // 2, button_y - timer_text.get_height() - 10))

    pygame.display.flip()
