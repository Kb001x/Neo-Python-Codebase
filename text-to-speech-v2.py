import pygame.mixer
import pygame
import sys

# Configuration
AUDIO_FILE = "speech.mp3"
WINDOW_SIZE = (300, 200)
BUTTON_RECT = pygame.Rect(100, 80, 100, 40)


def initialize():
    pygame.mixer.init()


def play_audio(channel, sound):
    return channel.play(sound)


def pause_audio(channel):
    channel.pause()


def unpause_audio(channel):
    channel.unpause()


def create_gui():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Audio Player")
    return screen


def main():
    initialize()

    sound = pygame.mixer.Sound(AUDIO_FILE)
    channel = sound.play()

    screen = create_gui()

    font = pygame.font.Font(None, 36)
    button_color = (0, 255, 0)

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if BUTTON_RECT.collidepoint(event.pos):
                    if not channel.get_busy():
                        channel = play_audio(channel, sound)
                    elif paused:
                        unpause_audio(channel)
                        paused = False
                    else:
                        pause_audio(channel)
                        paused = True

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, button_color, BUTTON_RECT)
        text = font.render("Play/Pause", True, (0, 0, 0))
        screen.blit(text, (90, 90))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
