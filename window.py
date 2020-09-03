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
background_image=pygame.image.load("map.png")
#background_image=pygame.transform.scale(background_image, (400, 300))

p = player()


def run():
    # Beginning Game Loop
    count=0
    while True:
        pygame.display.update()
        p.events()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        update(p)
        #window.fill((255, 0, 0))
        #pygame.draw.rect(window, (255, 255, 255), (145, 95, 110, 110))
        window.blit(background_image, [200-p.x, 150-p.y])
        if p.moveleft==True:
            window.blit(pygame.transform.flip(p.pictures[int(count/5)%6], True, False), (200-20, 150-40))
        else:
            window.blit(p.pictures[int(count / 5) % 6], (200 - 20, 150 - 40))
        pygame.display.flip()
        FramePerSec.tick(FPS)
        if p.moving==True:
            count+=1

