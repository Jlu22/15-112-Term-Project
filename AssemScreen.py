import pygame
from Model import Model

def assemInit(self):
    self.assemList = []
    self.assemUndo = []

def assemMousePressed(self, x, y):
    pass

def assemKeyPressed(self, keyCode, modifier):
    cubeVerts = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), 
                      (-1, -1, 1), (1, -1, 1),(1, 1, 1), (-1, 1, 1)] 
    cubeEdges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), 
                      (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    
    if keyCode == pygame.K_n:
        self.assemList.append(Model(self.width, self.height, self._keys, cubeVerts, cubeEdges))
    if keyCode == pygame.K_m:
        self.assemList = []
        self.mode = "menu"
    if keyCode == pygame.K_h:
        self.mode = "help"
    if keyCode == pygame.K_u and len(self.assemList) > 0:
        self.assemUndo.append(self.assemList.pop())
    if keyCode == pygame.K_r and len(self.assemUndo) > 0:
        self.assemList.append(self.assemUndo.pop())

def assemTimerFired(self, dt):
    for model in self.assemList:
        model.timerFired(dt)

def assemRedrawAll(self, screen):
    self.bgColor = (178, 170, 158)
    for model in self.assemList:
        model.redrawAll(screen)
    pygame.display.update((0, 50, 800, 400))