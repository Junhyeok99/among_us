import sys
import pygame

from pygame.locals import *
from graphic import render, Colors

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()

# window size parameter
WIDTH = 640
HEIGHT = 320

# Setup display with caption
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(Colors["WHITE"])

pygame.display.set_caption("Among us")

render(window)


def run():
    # Beginning Game Loop
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        FramePerSec.tick(FPS)
