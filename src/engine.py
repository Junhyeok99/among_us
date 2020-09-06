from src.setting import *


def calc_dist(p, missions):
    chk = None
    for o in missions.list:
        # TODO: p가 가진 미션 중에서 현재 미션이 있는지 체크
        if not o.is_clear:
            if (p.x - o.location[0]) ** 2 + (p.y - o.location[1]) ** 2 < 10000:
                o.color = YELLOW
                chk = o
            else:
                o.color = WHITE
    return chk


def update(p, bm):
    x = p.x
    y = p.y
    if p.move_left and bm[p.y, p.x]:
        p.x -= p.speed
    if p.move_right and bm[p.y, p.x]:
        p.x += p.speed
    if bm[p.y, p.x] == 0:
        p.y = y
        p.x = x
    x = p.x
    y = p.y
    if p.move_down and bm[p.y, p.x]:
        p.y += p.speed
    if p.move_up and bm[p.y, p.x]:
        p.y -= p.speed
    if bm[p.y, p.x] == 0:
        p.y = y
        p.x = x
