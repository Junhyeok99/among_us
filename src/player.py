import os
import pygame as pg

from src.utils import *
from src.setting import *


class Player:
    def __init__(self, x=200, y=150, speed=SPEED):
        # Movement Property
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.is_left = False

        self.speed = speed
        self.x = x
        self.y = y

        self.is_mission = False
        self.active_mission = None
        self.active_player = None

        self.images = []
        self.load_images()

    def load_images(self):
        dir_name = "../contents/character/"
        for file in os.listdir(dir_name):
            full_name = os.path.join(dir_name, file)
            p = pg.image.load(full_name)
            self.images.append(pg.transform.scale(p, (40, 80)))

    def events(self):
        if not self.is_mission:
            if extract_events(pg.KEYDOWN, pg.K_LEFT):
                self.move_left = True
            if extract_events(pg.KEYDOWN, pg.K_RIGHT):
                self.move_right = True
            if extract_events(pg.KEYDOWN, pg.K_DOWN):
                self.move_down = True
            if extract_events(pg.KEYDOWN, pg.K_UP):
                self.move_up = True
            if extract_events(pg.KEYUP, pg.K_LEFT):
                self.move_left = False
            if extract_events(pg.KEYUP, pg.K_RIGHT):
                self.move_right = False
            if extract_events(pg.KEYUP, pg.K_DOWN):
                self.move_down = False
            if extract_events(pg.KEYUP, pg.K_UP):
                self.move_up = False
            if extract_events(pg.KEYDOWN, pg.K_SPACE) and self.active_mission is not None:
                self.is_mission = True
                self.active_mission.is_on = True

        if extract_events(pg.MOUSEBUTTONDOWN, None):
            print(pygame.mouse.get_pos())
        if self.move_left:
            self.is_left = True
        if self.move_right:
            self.is_left = False

    def is_moving(self):
        if self.move_up or self.move_down or self.move_left or self.move_right:
            return True
        else:
            return False

    def change_color(self):
        for i in self.images:
            for x in range(i.get_size()[0]):
                for y in range(i.get_size()[1]):
                    origin = i.get_at((x, y))
                    i.set_at((x, y), (min(255, origin[0] + 150), origin[1], min(255, origin[2] + 150), origin[3]))
