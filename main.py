from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        self.land.LoadLands('txt/my_land.txt')
        base.camLens.setFov(90)
        self.hero = Hero((0, 10, 2), self.land)
        
game = Game()
game.run()        