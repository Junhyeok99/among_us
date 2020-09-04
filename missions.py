import pygame as pg

fuel_press = False
trash_press=False
def filling_fuel(p,o):
    full_amount = 100
    global fuel_press
    for event in pg.event.get():
        if event.type == pg.QUIT:
            o.count=0
            p.is_mission=False
        if event.type == pg.KEYDOWN:
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
    full_amount = 100
    global trash_press
    for event in pg.event.get():
        if event.type == pg.QUIT:
            o.count=0
            p.is_mission=False
        if event.type == pg.KEYDOWN:
            if event.key== pg.K_SPACE:
                trash_press = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                trash_press = False
    if trash_press == True:
        o.count += 1
    if o.count == full_amount:
        print("trashing mission clear")
        p.is_mission = False
        o.is_clear=True