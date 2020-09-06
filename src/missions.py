import os
import numpy as np
import pygame as pg

from src.utils import *
from src.engine import *


class Object:
    def __init__(self, name, loc, func, graphic):
        self.name = name
        self.mission = func
        self.display = graphic
        self.location = loc
        self.color = WHITE
        self.is_clear = False
        self.is_on = False

    def run(self):
        if self.mission():
            self.is_clear = True
            self.is_on = False
            self.color = WHITE
            return True

    def show(self, w):
        self.display(w)


class Mission:
    def __init__(self):
        # load file
        f_name = os.path.join("../data/maze_bm.data")
        self.maze_bm = np.loadtxt(f_name)

        # properties
        self.press = False
        self.count = 0

        self.list = []
        self.assign_missions()

    def filling_fuel(self):
        max_cnt = 300
        if extract_events(pg.KEYDOWN, pg.K_SPACE):
            self.press = True
        if extract_events(pg.KEYUP, pg.K_SPACE):
            self.press = False
        if self.press:
            self.count += 1
        if self.count == max_cnt:
            self.count = 0
            self.press = False
            return True

    def f_t_d_display(self, window):
        pg.draw.rect(window, BLACK, (100, 100, 300, 300))
        pg.draw.rect(window, YELLOW, (100, 100, self.count, 300))

    def trashing(self):
        max_cnt = 300
        if extract_events(pg.KEYDOWN, pg.K_SPACE):
            self.press = True
        if extract_events(pg.KEYUP, pg.K_SPACE):
            self.press = False
            self.count = 0
        if self.press:
            self.count += 1
        if self.count == max_cnt:
            self.count = 0
            self.press = False
            return True

    def data_download(self):
        max_cnt = 300
        if extract_events(pg.KEYDOWN, pg.K_SPACE):
            self.press = True
        if self.press:
            self.count += 1
        if self.count == max_cnt:
            self.count = 0
            self.press = False
            return True

    def assign_missions(self):
        self.list.append(Object("filling fuel", (300, 100), self.filling_fuel, self.f_t_d_display))
        self.list.append(Object("trashing", (660, 60), self.trashing, self.f_t_d_display))
        self.list.append(Object("data_download", (460, 260), self.data_download, self.f_t_d_display))

    def update(self, p):
        cur = None
        for m in self.list:
            if m.is_on:
                cur = m
        if extract_events(pg.KEYDOWN, pg.K_x) and cur is not None:
            cur.is_on = False
            self.count = 0
            self.press = False
            p.is_mission = False
        elif cur is not None:
            if cur.run():
                p.is_mission = False

# def maze(window, p, o):
#     maze_map = pg.image.load("contents/map/maze_map.png")
#     maze_map = (pg.transform.scale(maze_map, (200, 400)))
#     window.blit(maze_map, (150, 50))
#
#     o.maze_player.events()
#     update(o.maze_player, maze_bm)
#     window.blit(pg.transform.scale(o.maze_player.pictures[1], (20, 40)),
#                 (150 - 20 + o.maze_player.x * 20, 50 - 40 + o.maze_player.y * 40))
#     if o.maze_player.x == 10 and o.maze_player.y == 10:
#         print("maze mission clear")
#         p.is_mission = False
#         o.is_clear = True
