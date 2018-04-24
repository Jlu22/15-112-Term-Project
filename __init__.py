# file that initiates whole project

import pygame
from pygamegame import PygameGame
from MenuScreen import *
from ModelScreen import *
from AssemScreen import *
from HelpScreen import *

class PyCAD(PygameGame):
    
    def init(self):
        menuInit(self)
        createInit(self)
        assemInit(self)
        helpInit(self)
    
    def mousePressed(self, x, y):
        print(x, y)
        if self.mode == "menu":
            menuMousePressed(self, x, y)
        elif self.mode == "create":
            createMousePressed(self, x, y)
        elif self.mode == "assem":
            assemMousePressed(self, x, y)
        elif self.mode == "help":
            helpMousePressed(self, x, y)
    
    def mouseDrag(self, x, y):
        if self.mode == "create":
            for model in self.modelList:
                model.mouseDrag(x, y)
    
    def mouseMotion(self, x, y):
        if self.mode == "menu":
            pass
    
    def keyPressed(self, keyCode, modifier):
        if self.mode == "menu":
            menuKeyPressed(self, keyCode, modifier)
        elif self.mode == "create":
            createKeyPressed(self, keyCode, modifier)
        elif self.mode == "assem":
            assemKeyPressed(self, keyCode, modifier)
        elif self.mode == "help":
            helpKeyPressed(self, keyCode, modifier)
    
    def timerFired(self, dt):
        if self.mode == "menu":
            menuTimerFired(self, dt)
        elif self.mode == "create":
            createTimerFired(self, dt)
        elif self.mode == "assem":
            assemTimerFired(self, dt)

    def redrawAll(self, screen):
        if self.mode == "menu":
            menuRedrawAll(self, screen)
        elif self.mode == "create":
            createRedrawAll(self, screen)
        elif self.mode == "assem":
            assemRedrawAll(self, screen)
        elif self.mode == "help":
            helpRedrawAll(self, screen)
    
PyCAD(800, 500).run()