from pickle import dump, load

class Mapmanager:
    
    def __init__(self):
        self.modell = 'models/block.egg'
        self.t = loader.loadTexture('textures/green_earth.png')
        self.Start_new()

    def TWater(self):
        self.t = loader.loadTexture('textures/water.png')

    def TTree(self):
        self.t = loader.loadTexture('textures/tree.png')

    def TEarth(self):
        self.t = loader.loadTexture('textures/earth.png')

    def TFoliage(self):
        self.t = loader.loadTexture('textures/foliage.png')

    def TGrass(self):
        self.t = loader.loadTexture('textures/green_earth.png')

    def TCobblestone(self):
        self.t = loader.loadTexture('textures/cobblestone.png')

    def TBricks(self):
        self.t = loader.loadTexture('textures/stone_bricks.png')

    def Start_new(self):
        self.land = render.attachNewNode('Land')

    def AddBlock(self, pos, t):
        block = loader.loadModel(self.modell)
        block.setTexture(t)
        block.setPos(pos)
        block.reparentTo(self.land)
        block.setTag('Bl', str(pos))
    
    def LoadLands(self, land):
        self.Clear()
        with open(land) as f:
            y = 0
            for line in f:
                x = 0
                string = list(map(int, line.split()))
                for i in string:
                    for z in range(i+1):
                        self.AddBlock((x, y, z), t=self.t)
                
                    x += 1
                y += 1

    def Clear(self):
        self.land.removeNode()
        self.Start_new()

    def Empty(self, pos):
        blocks = self.FindBlocks(pos)
        if not blocks:
            return True
        else:
            return False

    def FindEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.Empty((x, y, z)):
            z += 1
        return (x, y, z)

    def FindBlocks(self, pos):
        return self.land.findAllMatches('=Bl=' + str(pos))
    
    def BlockBuild(self, pos, t):
        x, y, z = pos
        new_bl = self.FindEmpty(pos)
        if new_bl[2] <= z + 1:
            self.AddBlock(new_bl, t=self.t) 

    def BlockDestroy(self, pos):
        blocks = self.FindBlocks(pos)
        for block in blocks:
            block.removeNode()

    def BlockDsFrom(self, pos):
        x, y, z = self.FindEmpty(pos)
        pos = x, y, z-1
        blocks = self.FindBlocks(pos)
        for block in blocks:
            block.removeNode()

    def SaveMap(self):
        blocks = self.land.getChildren()
        with open('my_Bind', 'wb') as f:
            dump(len(blocks), f)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                dump(pos, f)
                dump(block.getTexture(), f)
                
    def LoadMap(self):
        self.Clear()
        with open('my_bind', 'rb') as f:
            blocks_count = load(f)
            for i in range(blocks_count):
                pos = load(f)
                texture = load(f)
                self.AddBlock(pos, t=texture)