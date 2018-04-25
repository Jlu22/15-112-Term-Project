import pygame
from Model import Model

def createInit(self):
    self.curModel = None
    self.modelMode = "view"
    self.sketchPoints = []
    self.sketchUndo = []

def createMousePressed(self, x, y):
    if self.modelMode == "view" and (20 <= x <= 90) and (10 <= y <= 40):
        self.modelMode = "sketch"
    elif self.modelMode == "sketch" and (50 <= y <= 450):
        self.sketchPoints.append((x,y))

def createKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_m:
        self.mode = "menu"
    if keyCode == pygame.K_h:
        self.mode = "help"
    if self.modelMode == "sketch":
        if keyCode == pygame.K_u and len(self.sketchPoints) > 0:
            self.sketchUndo.append(self.sketchPoints.pop())
        if keyCode == pygame.K_r and len(self.sketchUndo) > 0:
            self.sketchPoints.append(self.sketchUndo.pop())

def createTimerFired(self, dt):
    pass

def createRedrawAll(self, screen):
    drawOptions(self, screen)
    self.bgColor = (178, 0, 158)
    for point in self.sketchPoints:
        pygame.draw.circle(screen, (0, 0, 0), point, 5)
    if len(self.sketchPoints) >= 3:
        pygame.draw.polygon(screen, (0, 0, 0), self.sketchPoints, 2)
    pygame.display.update((0, 50, 800, 400))

def drawOptions(self, screen):
    pygame.draw.rect(screen, (217, 224, 247), (0, 0, 800, 50))
    pygame.draw.rect(screen, (255, 0, 0), (20,10,70,30))
    pygame.display.update((0, 0, 800, 50))