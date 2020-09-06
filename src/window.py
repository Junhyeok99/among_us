import sys

from src.player import *
from src.graphic import *
from src.missions import *
from pygame.locals import *


class Window:
    def __init__(self):
        # Initialize program
        pygame.init()
        self.FramePerSec = pygame.time.Clock()

        # Setup display with caption
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        # Load files
        bm = np.load('../data/map.npy')
        self.bm = bm.reshape(1000, 1000)

        # Graphic
        self.graphic = Graphic(self.window)

        # Player
        self.player = Player()

        # Mission
        self.mission = Mission()

    def run(self):
        # Beginning Game Loop
        count = 0
        while True:
            # updating display and quit event
            if extract_events(QUIT, None):
                pygame.quit()
                sys.exit()

            # execute missions
            self.player.events()
            self.mission.update(self.player)

            update(self.player, self.bm)

            # calculate distance between player and mission
            self.player.active_mission = calc_dist(self.player, self.mission)

            self.graphic.show(self.player, self.mission, count)

            if self.player.is_moving():
                count += 1
            self.FramePerSec.tick(FPS)
