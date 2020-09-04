import pygame as pg
from engine import *
fname = os.path.join("maze_bm.data")
maze_bm = np.loadtxt(fname)

fuel_press = False
trash_press=False
start_download=False
def filling_fuel(p,o):
    full_amount = 300
    global fuel_press
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                print("A")
                o.count = 0
                p.is_mission = False
            if event.key== pg.K_SPACE:
                fuel_press = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                fuel_press = False
    if fuel_press == True:
        o.count += 1
    if o.count == full_amount:
        print("fuel mission clear")
        p.is_mission = False
        o.is_clear=True

def trashing(p,o):
    full_amount = 300
    global trash_press
    for event in pg.event.get():
        if event.key == pg.K_a:
            print("A")
            o.count = 0
            p.is_mission = False
        if event.type == pg.KEYDOWN:
            if event.key== pg.K_SPACE:
                trash_press = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                trash_press = False
                o.count=0
    if trash_press == True:
        o.count += 1
    if o.count == full_amount:
        print("trashing mission clear")
        p.is_mission = False
        o.is_clear=True

def data_download(p,o):
    full_amount = 300
    global start_download
    for event in pg.event.get():
        if event.key == pg.K_a:
            print("A")
            start_download=False
            o.count = 0
            p.is_mission = False
        if event.type == pg.KEYDOWN:
            if event.key== pg.K_SPACE:
                start_download = True

    if start_download == True:
        o.count += 1
    if o.count == full_amount:
        print("data mission clear")
        p.is_mission = False
        o.is_clear=True

def maze(window, p,o):
    maze_map = pg.image.load("contents/map/maze_map.png")
    maze_map=(pg.transform.scale(maze_map, (200, 400)))
    window.blit(maze_map, (150, 50))

    o.maze_player.events()
    update(o.maze_player, maze_bm)
    window.blit(pg.transform.scale(o.maze_player.pictures[1],(20, 40)), (150-20+o.maze_player.x*20, 50-40 +o.maze_player.y*40))
    if o.maze_player.x==10 and o.maze_player.y==10:
        print("maze mission clear")
        p.is_mission = False
        o.is_clear=True