from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from direct.gui.OnscreenImage import OnscreenImage

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        self.land.LoadLands('txt/my_land.txt')
        base.camLens.setFov(90)
        self.hero = Hero((0, 10, 2), self.land)

        self.taskMgr.add(self.hero.Update, 'update')

        self.i = 0
        self.sky = ['textures/SkyMin.jpg', 'textures/SkyMinNight.jpg']
        self.image = OnscreenImage(parent=render2d, image=self.sky[0])
        base.cam.node().getDisplayRegion(0).setSort(20)

        self.taskMgr.doMethodLater(120, self.ChangeSky, 'changeSky')

    def ChangeSky(self, task):
        self.i = (self.i + 1) % len(self.sky)
        self.image.destroy()
        self.image = OnscreenImage(parent=render2d, image=self.sky[self.i])
        return task.again

game = Game()
game.run()