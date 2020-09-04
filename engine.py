import os
import random
import numpy as np
import pygame as pg

from setting import *




def calc_dist(p, objs):
    for o in objs:
        if (p.x-o.location[0])**2+(p.y-o.location[1])**2 < 10000:
            o.color=RED
        else:
            o.color=WHITE


def update(p,bm):

    x = p.x
    y = p.y
    if p.moveleft and bm[p.y, p.x]:
        p.x -= p.speed
    if p.moveright and bm[p.y, p.x]:
        p.x += p.speed
    if bm[p.y, p.x] == 0:
        p.y = y
        p.x = x
    x = p.x
    y = p.y
    if p.movedown and bm[p.y, p.x]:
        p.y += p.speed
    if p.moveup and bm[p.y, p.x]:
        p.y -= p.speed
    if bm[p.y, p.x] == 0:
        p.y = y
        p.x = x


class Player:
    def __init__(self, _x=200, _y=150, _speed=SPEED):
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.done = False
        self.pictures = []
        self.moving = False
        self.isleft = False
        self.is_mission=False
        self.missions = random.sample({0, 1, 2, 3, 4, 5}, 2)
        picture = pg.image.load("contents/character/1.png")
        self.pictures.append(pg.transform.scale(picture, (40, 80)))
        picture = pg.image.load("contents/character/2.png")
        self.pictures.append(pg.transform.scale(picture, (40, 80)))
        picture = pg.image.load("contents/character/3.png")
        self.pictures.append(pg.transform.scale(picture, (40, 80)))
        picture = pg.image.load("contents/character/4.png")
        self.pictures.append(pg.transform.scale(picture, (40, 80)))
        picture = pg.image.load("contents/character/5.png")
        self.pictures.append(pg.transform.scale(picture, (40, 80)))
        picture = pg.image.load("contents/character/6.png")
        self.pictures.append(pg.transform.scale(picture, (40, 80)))


    def events(self, is_close=False):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = event
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.moveleft = True
                if event.key == pg.K_a:
                    self.change_color()
                if event.key == pg.K_RIGHT:
                    self.moveright = True
                if event.key == pg.K_DOWN:
                    self.movedown = True
                if event.key == pg.K_UP:
                    self.moveup = True
                if event.key == pg.K_SPACE and is_close:
                    self.is_mission=True
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
        if self.moveleft or self.moveright or self.moveup or self.movedown:
            self.moving = True
        else:
            self.moving = False
        if self.moveleft:
            self.isleft = True
        if self.moveright:
            self.isleft = False

    def change_color(self):
        for i in self.pictures:
            for x in range(i.get_size()[0]):
                for y in range(i.get_size()[1]):
                    origin = i.get_at((x, y))
                    i.set_at((x, y), (min(255, origin[0] + 150), origin[1], min(255, origin[2] + 150), origin[3]))

class Object:
    def __init__(self, name, loc, mission_num):
        self.name = name
        self.mission = ""
        self.location = loc
        self.color = WHITE
        self.is_clear=False
        self.count=0
        self.mission_num=mission_num
        self.maze_player=Player(1, 1, 1)
    def interact(self):
        print(self.name, self.location)
