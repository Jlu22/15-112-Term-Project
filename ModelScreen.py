import pygame
from Model import Model

def createInit(self):
    self.modelList = []

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