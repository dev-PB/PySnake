import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 800
PIXEL_SIZE = 20


def main():
    pygame.init()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Snake")

if __name__ == "__main__":
    main()