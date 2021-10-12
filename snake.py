import pygame
import sys

WIN_WIDTH = 800
WIN_HEIGHT = 800
PIXEL_SIZE = 20

BG_COLOUR = (186, 222, 252)
BG_COLOUR_ALT = (98, 181, 248)
SNAKE_COLOUR = (50, 168, 82)

class Snake():
    def __init__(self, x, y):
        self.length = 1
        self.body = [[x, y] ]
        self.direction = {"x": -1, "y": 0}

    def move(self):
        head = self.body[0]
        next_pos = [ (head[0] + (self.direction["x"] * PIXEL_SIZE)), (head[1] + (self.direction["y"] * PIXEL_SIZE)) ]

        if next_pos in self.body:
            pass

        else:
            self.body.insert(0, next_pos)
            self.body.pop()

    def set_direction(self, new_direction):
        self.direction = new_direction

    def draw(self, window):
        for body_part in self.body:
            snake_pixel = pygame.Rect(body_part[0], body_part[1], PIXEL_SIZE, PIXEL_SIZE)
            pygame.draw.rect(window, SNAKE_COLOUR, snake_pixel)



def draw_background(window):
    for x in range(0, WIN_WIDTH, PIXEL_SIZE):
        for y in range(0, WIN_HEIGHT, PIXEL_SIZE):
            tile = pygame.Rect(x, y, PIXEL_SIZE, PIXEL_SIZE)

            # Alternate the colour of the background tiles
            if ((x + y) / PIXEL_SIZE) % 2 == 0:
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
    while running:
        clock.tick(20)
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
    