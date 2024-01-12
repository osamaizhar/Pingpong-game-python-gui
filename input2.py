import pygame
import pygame_gui

pygame.init()

# Set up the Pygame window
window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame GUI Input')

# Create a Pygame GUI manager
gui_manager = pygame_gui.UIManager((800, 600))

# Create an input box
input_box = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((300, 275), (200, 50)),
    manager=gui_manager
)

# Set up the Pygame clock
clock = pygame.time.Clock()

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                # Get the input from the text box
                input_text = event.text
                print(f"Input: {input_text}")
                input_box.set_text('')
        gui_manager.process_events(event)

    # Update the Pygame GUI manager
    gui_manager.update(clock.tick(60) / 1000.0)

    # Draw the Pygame GUI manager
    gui_manager.draw_ui(window_surface)

    # Update the Pygame display
    pygame.display.update()
