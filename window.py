import sys
import pygame

from pygame.locals import *
from engine import *
from missions import *
# Initialize program
pygame.init()

# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()

# window size parameter
WIDTH = 500
HEIGHT = 500

# Setup display with caption
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Among us")
background_image = pygame.image.load("contents/map/map.png")
# background_image=pygame.transform.scale(background_image, (400, 300))

p = Player()
objs = [
    Object("1-1", (300, 100), 1),
    Object("2-1", (660, 60), 2),
    Object("2-2", (460, 260), 3),
    Object("3-1", (60, 660), 4),
    Object("4-1", (660, 700), 5),
    Object("4-2", (660, 460), 6),
]

def run():
    # Beginning Game Loop
    count = 0
    is_close=False
    print("player missions")
    for m in p.missions:
        print(objs[m].name)
    while True:
        pygame.display.update()
        if not p.is_mission:
            p.events(is_close)
        if not p.is_mission:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        update(p)

        #calculate distance and is_clear to check whether we can start a mission
        calc_dist(p, objs)
        is_close = False
        for o in objs:
            if o.color==RED and o.is_clear==False:
                is_close=True

        #show background image
        window.blit(background_image, [210 - p.x, 160 - p.y])
        for o in objs:
            pygame.draw.rect(window, o.color, (o.location[0] - p.x + 200, o.location[1] - p.y + 150, 40, 40))
        if p.isleft:
            window.blit(pygame.transform.flip(p.pictures[int(count / 5) % 6], True, False), (200 - 20, 150 - 70))
        else:
            window.blit(p.pictures[int(count / 5) % 6], (200 - 20, 150 - 70))

        for o in objs:
            if o.color==RED and p.is_mission:
                if o.mission_num==1:
                    filling_fuel(p,o)
                elif o.mission_num==2:
                    trashing(p, o)
                elif o.mission_num==3:
                    p.is_mission = False
                    pass
                elif o.mission_num==4:
                    p.is_mission = False
                    pass
                elif o.mission_num==5:
                    p.is_mission = False
                    pass
                elif o.mission_num==6:
                    p.is_mission = False
                    pass
        pygame.display.flip()
        FramePerSec.tick(FPS)
        if p.moving:
            count += 1
