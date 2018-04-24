# file that initiates whole project

import pygame
import math
from pygamegame import PygameGame
from Camera import Camera
from Model import Model

class PyCAD(PygameGame):
    
    def init(self):
        self.modelList = []
    
    def mousePressed(self, x, y):
        print(x, y)
        if self.mode == "menu":
            self.menuMousePressed(x, y)
        elif self.mode == "create":
            self.createMousePressed(x, y)
        elif self.mode == "assem":
            self.assemMousePressed(x, y)
        elif self.mode == "help":
            self.helpMousePressed(x, y)
    
    def mouseDrag(self, x, y):
        if self.mode == "create":
            for model in self.modelList:
                model.mouseDrag(x, y)
    
    def mouseMotion(self, x, y):
        if self.mode == "menu":
            pass
    
    def keyPressed(self, keyCode, modifier):
        if self.mode == "menu":
            self.menuKeyPressed(keyCode, modifier)
        elif self.mode == "create":
            self.createKeyPressed(keyCode, modifier)
        elif self.mode == "assem":
            self.assemKeyPressed(keyCode, modifier)
        elif self.mode == "help":
            self.helpKeyPressed(keyCode, modifier)
    
    def timerFired(self, dt):
        if self.mode == "menu":
            self.menuTimerFired(dt)
        elif self.mode == "create":
            self.createTimerFired(dt)
        elif self.mode == "assem":
            self.assemTimerFired(dt)

    def redrawAll(self, screen):
        if self.mode == "menu":
            self.menuRedrawAll(screen)
        elif self.mode == "create":
            self.createRedrawAll(screen)
        elif self.mode == "assem":
            self.assemRedrawAll(screen)
        elif self.mode == "help":
            self.helpRedrawAll(screen)

##          Menu          ##

    def menuMousePressed(self, x, y):
        if (170 <= x <= 380) and (280 <= y <= 340):
            self.mode = "create"
        elif (430 <= x <= 650) and (280 <= y <= 340):
            self.mode = "assem"
        elif (170 <= x <= 380) and (360 <= y <= 420):
            self.mode = "help"
        #elif (430 <= x <= 650) and (360 <= y <= 420):
    
    def menuKeyPressed(self, keyCode, modifier):
        pass
    
    def menuTimerFired(self, dt):
        pass
    
    def menuRedrawAll(self, screen):
        self.bgColor = (217, 224, 247)
        pygame.draw.rect(screen, (255, 0, 0), (170, 280, 210, 60))
        pygame.draw.rect(screen, (0, 0, 255), (430, 280, 210, 60))
        pygame.draw.rect(screen, (0, 255, 100), (170, 360, 210, 60))
        pygame.draw.rect(screen, (100, 100, 0), (430, 360, 210, 60))
        pygame.display.flip()

##          Create Model          ##

    def createMousePressed(self, x, y):
        pass
    
    def createKeyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_n:
            self.modelList.append(Model(self.width, self.height, self._keys))
        if keyCode == pygame.K_m:
            self.modelList = []
            self.mode = "menu"
    
    def createTimerFired(self, dt):
        for model in self.modelList:
            model.timerFired(dt)
    
    def createRedrawAll(self, screen):
        self.bgColor = (178, 0, 158)
        for model in self.modelList:
            model.redrawAll(screen)
        pygame.display.update((0, 50, 800, 400))

##          Assembly          ##

    def assemMousePressed(self, x, y):
        pass
    
    def assemKeyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_n:
            self.modelList.append(Model(self.width, self.height, self._keys))
        if keyCode == pygame.K_m:
            self.modelList = []
            self.mode = "menu"
    
    def assemTimerFired(self, dt):
        for model in self.modelList:
            model.timerFired(dt)
    
    def assemRedrawAll(self, screen):
        self.bgColor = (178, 170, 158)
        for model in self.modelList:
            model.redrawAll(screen)
        pygame.display.update((0, 50, 800, 400))

##          Help Screen          ##

    def helpMousePressed(self, x, y):
        pass
    
    def helpKeyPressed(self, keyCode, modifier):
        pass
    
    def helpRedrawAll(self, screen):
        pass
    
PyCAD(800, 500).run()
