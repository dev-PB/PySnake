import pygame
import sys
import random

WIN_WIDTH = 800
WIN_HEIGHT = 800
PIXEL_SIZE = 20

BG_COLOUR = (186, 222, 252)
BG_COLOUR_ALT = (98, 181, 248)
SNAKE_COLOUR = (50, 168, 82)
GOAL_COLOUR = (240, 97, 36)



def get_random_location():
        x = random.randint(0, (WIN_WIDTH / PIXEL_SIZE)) * PIXEL_SIZE
        y = random.randint(0, (WIN_HEIGHT / PIXEL_SIZE)) * PIXEL_SIZE
        return [x, y]


class Snake():
    def __init__(self, x, y):
        self.length = 1
        self.body = [[x, y] ]
        self.direction = {"x": -1, "y": 0}

    def get_head(self):
        return self.body[0]

    def get_next_position(self):
        head = self.get_head()
        return [ (head[0] + (self.direction["x"] * PIXEL_SIZE)), (head[1] + (self.direction["y"] * PIXEL_SIZE)) ]

    def move(self):
        next_pos = self.get_next_position()

        if len(self.body) > 1 and next_pos in self.body:
            pass

        else:
            self.body.insert(0, next_pos)
            self.body.pop()
    
    def grow(self):
        self.body.insert(0,  self.get_next_position())

    def set_direction(self, new_direction):
        self.direction = new_direction

    def draw(self, window):
        for body_part in self.body:
            snake_pixel = pygame.Rect(body_part[0], body_part[1], PIXEL_SIZE, PIXEL_SIZE)
            pygame.draw.rect(window, SNAKE_COLOUR, snake_pixel)

class Goal():
    def __init__(self):
        self.location = get_random_location()

    def get_location(self):
        return self.location

    def set_location(self, new_pos):
        self.location = new_pos

    def draw(self, window):
        goal_pixel = pygame.Rect(self.location[0], self.location[1], PIXEL_SIZE, PIXEL_SIZE)
        pygame.draw.rect(window, GOAL_COLOUR, goal_pixel)



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

def input_listener(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.set_direction({"x": 0, "y": -1})

            elif event.key == pygame.K_RIGHT:
                player.set_direction({"x": 1, "y": 0})

            elif event.key == pygame.K_DOWN:
                player.set_direction({"x": 0, "y": 1})

            elif event.key == pygame.K_LEFT:
                player.set_direction({"x": -1, "y": 0})
            

def main():
    pygame.init()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Snake")

    draw_background(window)
    snake = Snake(400, 400)
    goal = Goal()

    # Game loop
    running = True
    while running:
        clock.tick(10)
        
        input_listener(snake)
        snake.move()
        
        if snake.get_head() == goal.get_location():
            snake.grow()
            goal.set_location(get_random_location())

        # Draw elements
        draw_background(window)
        snake.draw(window)
        goal.draw(window)

        pygame.display.update()
        

if __name__ == "__main__":
    main()
    