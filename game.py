from direct.showbase.ShowBase import ShowBase
from map_manager import MapManager


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        base.camLens.setFov(90)
        land = MapManager()

game = Game()
game.run()