import pygame


def extract_events(typ, key=None):
    evs = []
    chk = False
    for event in pygame.event.get():
        if event.type == typ and key is None:
            chk = True
        elif event.type == typ and key is not None and event.key == key:
            chk = True
        elif event.type == pygame.MOUSEMOTION:
            continue
        else:
            evs.append(event)

    for event in evs:
        pygame.event.post(event)

    return chk
