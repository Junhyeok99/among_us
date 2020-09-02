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
        p.events()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        update(p)
        window.fill((255, 0, 0))
        pygame.draw.rect(window, (255, 255, 255), (145, 95, 110, 110))
        window.blit(p.picture, (p.x-48, p.y-31))
        pygame.display.flip()
        FramePerSec.tick(FPS)
