# file that initiates whole project

import pygame
from pygamegame import PygameGame
from MenuScreen import *
from ModelScreen import *
from AssemScreen import *
from HelpScreen import *
from SaveScreen import *
from SaveFiles import checkSaved
  
class PyCAD(PygameGame):
    
    def init(self):
        menuInit(self)
        createInit(self)
        assemInit(self)
        helpInit(self)
        saveInit(self)
        checkSaved(self)
    
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
        elif self.mode == "save":
            saveMousePressed(self, x, y)
    
    def mouseDrag(self, x, y):
        if self.mode == "assem":
            for model in self.assemList:
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
        elif self.mode == "save":
            saveKeyPressed(self, keyCode, modifier)
    
    def timerFired(self, dt):
        if self.mode == "menu":
            menuTimerFired(self, dt)
        elif self.mode == "create":
            createTimerFired(self, dt)
        elif self.mode == "assem":
            assemTimerFired(self, dt)
        elif self.mode == "save":
            saveTimerFired(self, dt)

    def redrawAll(self, screen):
        if self.mode == "menu":
            menuRedrawAll(self, screen)
        elif self.mode == "create":
            createRedrawAll(self, screen)
        elif self.mode == "assem":
            assemRedrawAll(self, screen)
        elif self.mode == "help":
            helpRedrawAll(self, screen)
        elif self.mode == "save":
            saveRedrawAll(self, screen)
    
PyCAD(800, 500).run()