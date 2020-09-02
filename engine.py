import pygame as pg
from setting import *


class start:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WINDOW_SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

class player:
    def __init__(self):
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        self.x = 0
        self.y = 0
        self.speed = SPEED
        self.done = False

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.moveleft = True
                if event.key == pg.K_RIGHT:
                    self.moveright = True
                if event.key == pg.K_DOWN:
                    self.movedown = True
                if event.key == pg.K_UP:
                    self.moveup = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.moveleft = False
                if event.key == pg.K_RIGHT:
                    self.moveright = False
                if event.key == pg.K_DOWN:
                    self.movedown = False
                if event.key == pg.K_UP:
                    self.moveup = False
                    
    def update(self):
        if self.moveleft == True:
            self.x -= self.speed
        if self.moveright == True:
            self.x += self.speed
        if self.movedown == True:
            self.y += self.speed
        if self.moveup == True:
            self.y -= self.speed


g = start()
p = player()

while not p.done:
    g.clock.tick(FPS)
    g.screen.fill(WHITE)
    p.events()
    p.update()
    pg.draw.circle(g.screen, GREEN, (p.x + 20, p.y + 20), 5)
    pg.display.flip()

pg.quit()
