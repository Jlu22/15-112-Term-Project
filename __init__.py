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
        if self.mode == "menu":
            self.menuMousePressed(x, y)
    
    def mouseDrag(self, x, y):
        if self.mode == "create":
            for model in self.modelList:
                model.mouseDrag( x, y)
    
    def mouseMotion(self, x, y):
        if self.mode == "menu":
            pass
    
    def keyPressed(self, keyCode, modifier):
        if self.mode == "menu":
            self.menuKeyPressed(keyCode, modifier)
        elif self.mode == "create":
            self.createKeyPressed(keyCode, modifier)
    
    def timerFired(self, dt):
        if self.mode == "menu":
            self.menuTimerFired(dt)
        elif self.mode == "create":
            self.createTimerFired(dt)

    def redrawAll(self, screen):
        if self.mode == "menu":
            self.menuRedrawAll(screen)
        elif self.mode == "create":
            self.createRedrawAll(screen)

##          Menu          ##
    
    def menuInit(self):
        pass
        
    def menuMousePressed(self, x, y):
        self.mode = "create"
    
    def menuKeyPressed(self, keyCode, modifier):
        pass
    
    def menuTimerFired(self, dt):
        pass
    
    def menuRedrawAll(self, screen):
        self.bgColor = (217, 224, 247)
        pygame.draw.rect(screen, (255, 0, 0), (300, 270, 200, 50))
        pygame.draw.rect(screen, (0, 0, 255), (300, 350, 200, 50))
        pygame.display.flip()

##          Create Model          ##

    def createTimerFired(self, dt):
        for model in self.modelList:
            model.timerFired(dt)
    
    def createKeyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_n:
            self.modelList.append(Model(self.width, self.height, self._keys))
        if keyCode == pygame.K_m:
            self.modelList = []
            self.mode = "menu"
    
    def createRedrawAll(self, screen):
        self.bgColor = (178, 170, 158)
        for model in self.modelList:
            model.redrawAll(screen)
        pygame.display.update((0, 50, 800, 400))

##          Assembly          ##


##          Help Screen          ##

PyCAD(800, 500).run()
