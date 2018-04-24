import pygame
from Model import Model

def assemInit(self):
    pass

def assemMousePressed(self, x, y):
    pass

def assemKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_n:
        self.modelList.append(Model(self.width, self.height, self._keys))
    if keyCode == pygame.K_m:
        self.modelList = []
        self.mode = "menu"
    if keyCode == pygame.K_h:
        self.mode = "help"

def assemTimerFired(self, dt):
    for model in self.modelList:
        model.timerFired(dt)

def assemRedrawAll(self, screen):
    self.bgColor = (178, 170, 158)
    for model in self.modelList:
        model.redrawAll(screen)
    pygame.display.update((0, 50, 800, 400))