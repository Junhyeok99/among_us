import pygame as pg
from setting import *
import numpy as np
import os

fname = os.path.join("map.data")
bm = np.loadtxt(fname)
bm = bm.reshape(300, 400)


def update(p):
    p.events()
    x = p.x
    y = p.y
    if p.moveleft and bm[p.y, p.x]:
        p.x -= p.speed
    if p.moveright and bm[p.y, p.x]:
        p.x += p.speed
    if p.movedown and bm[p.y, p.x]:
        p.y += p.speed
    if p.moveup and bm[p.y, p.x]:
        p.y -= p.speed
    if bm[p.y, p.x] == 0:
        p.y = y
        p.x = x


class player:
    def __init__(self):
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        self.x = 200
        self.y = 150
        self.speed = SPEED
        self.done = False
        picture=pg.image.load("character.png")
        self.picture=pg.transform.scale(picture, (96, 62))
       # self.picture=self.picture.convert()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = event
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
        if self.done:
            pg.event.post(self.done)
            self.done = False
