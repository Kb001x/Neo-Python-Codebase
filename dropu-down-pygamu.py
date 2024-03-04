import pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 32)

# Menu configuration
menu_items = ["Option 1", "Option 2", "Option 3"]
menu_active = False
menu_rect = pygame.Rect(50, 50, 140, 32)
item_height = 32

# Colors
default_color = (0, 128, 255)
hover_color = (100, 149, 237)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_rect.collidepoint(event.pos):
                menu_active = not menu_active
            else:
                menu_active = False

    # Clear screen
    screen.fill((30, 30, 30))

    # Draw menu
    pygame.draw.rect(screen, default_color, menu_rect)
    menu_text = font.render(menu_items[0], True, (255, 255, 255))
    screen.blit(menu_text, (menu_rect.x + 5, menu_rect.y + 5))

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw menu items
    if menu_active:
        for i, item in enumerate(menu_items):
            item_rect = pygame.Rect(menu_rect.x, menu_rect.y + (i + 1) * item_height, menu_rect.width, item_height)

            # Change color if mouse is hovering over item
            color = hover_color if item_rect.collidepoint(mouse_pos) else default_color

            pygame.draw.rect(screen, color, item_rect)
            item_text = font.render(item, True, (255, 255, 255))
            screen.blit(item_text, (item_rect.x + 5, item_rect.y + 5))

    pygame.display.flip()

pygame.quit()
