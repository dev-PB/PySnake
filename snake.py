import pygame
import sys

WIN_WIDTH = 800
WIN_HEIGHT = 800
PIXEL_SIZE = 20

BG_COLOUR = (186, 222, 252)
BG_COLOUR_ALT = (98, 181, 248)


def draw_background(window):
    for x in range(0, WIN_WIDTH, PIXEL_SIZE):
        for y in range(0, WIN_HEIGHT, PIXEL_SIZE):
            tile = pygame.Rect(x, y, PIXEL_SIZE, PIXEL_SIZE)

            # Alternate the colour of the background tiles
            if ((x + y) / 20) % 2 == 0:
                colour = BG_COLOUR
            else:
                colour = BG_COLOUR_ALT

            pygame.draw.rect(window, colour, tile)
            
            

def main():
    pygame.init()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Snake")

    draw_background(window)

    # Game loop
    running = True
    while (running):
        clock.tick(20)
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
    