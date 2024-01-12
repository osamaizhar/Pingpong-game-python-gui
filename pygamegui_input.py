import pygame
import pygame_gui

pygame.init()
def input_screen():

    # Set up the Pygame window
    window_surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pygame GUI Input')

    # Create a Pygame GUI manager
    gui_manager = pygame_gui.UIManager((800, 600))

    # Create a label for the title
    title_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((150, 150), (500, 50)),
        text='Players Enter Your Names!',
        manager=gui_manager
    )

    # Create input boxes and labels for Player One and Player Two
    player_one_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((150, 250), (100, 50)),
        text='Player One:',
        manager=gui_manager
    )

    player_one_input_box = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((250, 250), (200, 50)),
        manager=gui_manager
    )

    player_two_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((150, 325), (100, 50)),
        text='Player Two:',
        manager=gui_manager
    )

    player_two_input_box = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((250, 325), (200, 50)),
        manager=gui_manager
    )

    # Create a submit button
    submit_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((350, 400), (100, 50)),
        text='Submit',
        manager=gui_manager
    )

    # Set up the Pygame clock
    clock = pygame.time.Clock()
    list1=[]
    # Start the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    # Get the input from the text boxes
                    player_one_input_text = player_one_input_box.get_text()
                    player_two_input_text = player_two_input_box.get_text()
                    print(f"Player One: {player_one_input_text}")
                    print(f"Player Two: {player_two_input_text}")
                    list1.append(player_one_input_text)
                    list1.append(player_two_input_text)
            gui_manager.process_events(event)

        # Update the Pygame GUI manager
        gui_manager.update(clock.tick(60) / 1000.0)

        # Draw the Pygame GUI manager
        gui_manager.draw_ui(window_surface)

        # Update the Pygame display
        pygame.display.update()
        # Return the player names if the submit button has been pressed
        if len(list1) == 2:
            return tuple(list1)
    


if __name__ == "__main__":
    print(input_screen())