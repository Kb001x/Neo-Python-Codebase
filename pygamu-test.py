import pygame

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 32)

# Text box variables
text = ''
text_box_active = False
text_box_rect = pygame.Rect(300, 250, 200, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
line_height = font.get_height()

# Function to split text into lines
def wrap_text(text, font, max_width):
    words = text.replace('\n', ' \n ').split(' ')
    lines = []
    current_line = ''

    for word in words:
        if word == "\n":  # Manual line break
            lines.append(current_line)
            current_line = ''
        else:
            test_line = current_line + word + ' '
            # Check if adding the next word exceeds the width
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '

    lines.append(current_line)  # Add the last line
    return lines

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_box_rect.collidepoint(event.pos):
                text_box_active = not text_box_active
            else:
                text_box_active = False
            color = color_active if text_box_active else color_inactive

        # Handle text input
        if event.type == pygame.KEYDOWN:
            if text_box_active:
                if event.key == pygame.K_RETURN:
                    text += '\n'
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Clear screen
    screen.fill((30, 30, 30))

    # Wrap the text and render it
    wrapped_text = wrap_text(text, font, text_box_rect.width - 10)
    y = text_box_rect.top + 5
    for line in wrapped_text:
        txt_surface = font.render(line, True, color)
        screen.blit(txt_surface, (text_box_rect.left + 5, y))
        y += line_height

    # Resize the text box height
    text_box_rect.height = max(32, len(wrapped_text) * line_height + 10)

    # Draw the text box
    pygame.draw.rect(screen, color, text_box_rect, 2)

    pygame.display.flip()

pygame.quit()
