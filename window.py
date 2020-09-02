import sys
import pygame

from pygame.locals import *
from engine import player, update

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()

# window size parameter
WIDTH = 400
HEIGHT = 300

# Setup display with caption
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Among us")
p = player()


def run():
    # Beginning Game Loop
    while True:
        pygame.display.update()
        window.fill((255, 255, 255))
        p.events()
        update(p)
        pygame.draw.circle(window, (0, 0, 0), (p.x + 20, p.y + 20), 5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        FramePerSec.tick(FPS)
