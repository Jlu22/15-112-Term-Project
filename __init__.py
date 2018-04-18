import pygame
import math
from pygamegame import PygameGame
from Camera import Camera
from Model import Model

class PyCAD(PygameGame):
    
    def init(self):
        pass
    
    def mousePressed(self, x, y):
        if self.mode == "menu":
            self.menuMousePressed(x, y)
    
    def mouseDrag(self, x, y):
        if self.mode == "menu":
            return
    
    def mouseMotion(self, x, y):
        if self.mode == "menu":
            pass
    
    def keyPressed(self, keyCode, modifier):
        if self.mode == "menu":
            self.menuKeyPressed(keyCode, modifier)
    
    def timerFired(self, dt):
        if self.mode == "menu":
            self.menuTimerFired(dt)

    def redrawAll(self, screen):
        if self.mode == "menu":
            self.menuRedrawAll(screen)

##          Menu          ##
    
    def menuInit(self):
        pass
        
    def menuMousePressed(self, x, y):
        pass
    
    def menuKeyPressed(self, keyCode, modifier):
        pass
    
    def menuTimerFired(self, dt):
        pass
    
    def menuRedrawAll(self, screen):
        pass

##          Create Model          ##


##          Assembly          ##


##          Help Screen          ##

PyCAD(800, 500).run()
