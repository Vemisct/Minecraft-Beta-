from direct.task import Task

class Hero:

    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.mode = True
        self.FirstMode()
        self.Events()
        self.Is_Jump = False
        self.JumpSpeed = 0.3
        self.Gravity = 0.02
        self.JumpVelocity = 0
        self.stepS = loader.loadSfx('Voicy_Step4 - polarbear.mp3')

    def Events(self):
        base.accept('tab', self.ChangeCameraMode)
        base.accept('l', self.turnL)
        base.accept('l' + '-repeat', self.turnL)
        base.accept('k', self.turnR)
        base.accept('k' + '-repeat', self.turnR)
        base.accept('control', self.turnUp)
        base.accept('control' + '-repeat', self.turnUp)
        base.accept('shift', self.turnDown)
        base.accept('shift' + '-repeat', self.turnDown)
        base.accept('w', self.F)
        base.accept('w' + '-repeat', self.F)
        base.accept('s', self.B)
        base.accept('s' + '-repeat', self.B)
        base.accept('d', self.R)
        base.accept('d' + '-repeat', self.R)
        base.accept('a', self.L)
        base.accept('a' + '-repeat', self.L)
        base.accept('u', self.Up)
        base.accept('u' + '-repeat', self.Up)
        base.accept('i', self.Down)
        base.accept('i' + '-repeat', self.Down)
        base.accept('space', self.Jump)
        base.accept('caps_lock', self.ChangeMode)
        base.accept('b', self.Build)
        base.accept('r', self.Destroy)
        base.accept('c', self.land.SaveMap)
        base.accept('v', self.land.LoadMap)
        base.accept('1', self.land.TWater)
        base.accept('2', self.land.TEarth)
        base.accept('3', self.land.TGrass)
        base.accept('4', self.land.TBricks)
        base.accept('5', self.land.TCobblestone)
        base.accept('6', self.land.TTree)
        base.accept('7', self.land.TFoliage)

    def FirstMode(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setH(180)
        base.camera.setPos(0, 0, 1)
        self.cameraOn = True

    def FreeMode(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(- pos[0], - pos[1], - pos[2] - 3)
        base.enableMouse()
        base.camera.reparentTo(render)
        self.cameraOn = False

    def ChangeCameraMode(self):
        if self.cameraOn:
            self.FreeMode()
        else:
            self.FirstMode()

    def turnL(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turnR(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def turnUp(self):
        self.hero.setP((self.hero.getP() + 5) % 360)
    
    def turnDown(self):
        self.hero.setP((self.hero.getP() - 5) % 360)

    def FreeMove(self, angle):
        pos = self.LookAt(angle)
        self.hero.setPos(pos)

    def FirstMove(self, angle):
        pos = self.LookAt(angle)
        if self.land.Empty(pos):
            pos = self.land.FindEmpty(pos)
            self.hero.setPos(pos)
        
    def LookAt(self, angle):
        fx, fy, fz = list(map(int, self.hero.getPos()))
        dx, dy = self.CheckDir(angle)
        return fx + dx, fy + dy, fz

    def CheckDir(self, angle):
        if 0 <= angle <= 20:
            return 0, -1
        elif angle <= 65:
            return 1, -1
        elif angle <= 110:
            return 1, 0
        elif angle <= 155:
            return 1, 1
        elif angle <= 200:
            return 0, 1
        elif angle <= 245:
            return -1, 1
        elif angle <= 290:
            return -1, 0
        elif angle <= 335:
            return -1, -1
        elif angle <= 360:
            return 0, -1
        
    def Move(self, angle):
        if self.mode:
            self.FreeMove(angle)
        else:
            self.FirstMove(angle)
        if not self.stepS.status() == self.stepS.PLAYING:  
            self.stepS.play()
            
    def F(self):
        angle = (self.hero.getH()) % 360
        self.Move(angle)

    def B(self):
        angle = (self.hero.getH()+180) % 360
        self.Move(angle)

    def R(self):
        angle = (self.hero.getH()+270) % 360
        self.Move(angle)

    def L(self):
        angle = (self.hero.getH()+90) % 360
        self.Move(angle)

    def Up(self):
        self.hero.setZ(self.hero.getZ() + 1) 

    def Down(self):
        self.hero.setZ(self.hero.getZ() - 1)

    def Jump(self):
        if not self.Is_Jump:
            self.Is_Jump = True
            self.JumpVelocity = self.JumpSpeed
    
    def ChangeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    def Build(self):
        angle = (self.hero.getH()) % 360
        pos = self.LookAt(angle)
        if self.mode:
            self.land.AddBlock(pos, self.land.t)
        else:
            self.land.BlockBuild(pos, self.land.t)

    def Destroy(self):
        angle = (self.hero.getH()) % 360
        pos = self.LookAt(angle)
        if self.mode:
            self.land.BlockDestroy(pos)
        else:
            self.land.BlockDsFrom(pos)

    def Update(self, task):
        if self.mode == False:
            pos = self.hero.getPos()
            if self.Is_Jump:
                pos.z += self.JumpVelocity
                self.JumpVelocity -= self.Gravity
                ground = self.land.FindEmpty(map(int, pos))
                if pos.z <= ground[2]:
                    pos.z = ground[2]
                    self.Is_Jump = False
                    self.JumpVelocity = 0
                self.hero.setPos(pos)
        return Task.cont
    