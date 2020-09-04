import pygame


def extract_events(typ, key, func):
    evs = []
    for event in pygame.event.get():
        if event.type == typ and event.key == key:
            func()
        else:
            evs.append(event)

    for event in evs:
        pygame.event.post(event)
