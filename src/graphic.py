import pygame as pg


class Graphic:
    def __init__(self, window):
        # load files
        self.background_image = pg.image.load("../contents/map/map.png")

        # window properties
        self.window = window

    def show(self, player, missions, count):
        # background image
        pg.display.update()
        self.window.blit(self.background_image, [210 - player.x, 160 - player.y])

        # Mission spot
        for m in missions.list:
            loc = (m.location[0] - player.x + 200, m.location[1] - player.y + 150, 40, 40)
            pg.draw.rect(self.window, m.color, loc, 3)

        # player
        p_image = player.images[int(count / 5) % 6]
        if player.is_left:
            self.window.blit(pg.transform.flip(p_image, True, False), (200 - 20, 150 - 70))
        else:
            self.window.blit(p_image, (200 - 20, 150 - 70))

        # Missions
        for m in missions.list:
            if m.is_on:
                m.show(self.window)

        pg.display.flip()
