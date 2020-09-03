import sys
import pygame

from pygame.locals import *
from engine import *

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
background_image = pygame.image.load("map.png")
# background_image=pygame.transform.scale(background_image, (400, 300))

p = Player()
objs = [Object("test", (150, 150))]


def run():
    # Beginning Game Loop
    count = 0
    while True:
        pygame.display.update()
        p.events()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        update(p)
        calc_dist(p, objs)
        # window.fill((255, 0, 0))
        # pygame.draw.rect(window, (255, 255, 255), (145, 95, 110, 110))
        window.blit(background_image, [210 - p.x, 160 - p.y])
        for o in objs:
            pygame.draw.rect(window, o.color, (o.location[0] - p.x + 200, o.location[1] - p.y + 150, 5, 5))
        if p.isleft:
            window.blit(pygame.transform.flip(p.pictures[int(count / 5) % 6], True, False), (200 - 20, 150 - 70))
        else:
            window.blit(p.pictures[int(count / 5) % 6], (200 - 20, 150 - 70))
        pygame.display.flip()
        FramePerSec.tick(FPS)
        if p.moving:
            count += 1
