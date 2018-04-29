import pygame
from Model import Model
from Calculations import calculateVerts, calculateEdges

def createInit(self):
    self.curModel = None
    self.modelMode = "view"
    self.sketchPoints = []
    self.sketchUndo = []
    self.tmpSketchPoints = []
    self.tmpSketchUndo = []
    self.sketchError = False
    self.findDepth = False

def createMousePressed(self, x, y):
    if self.modelMode == "view" and (20 <= x <= 90) and (10 <= y <= 40):
        self.sketchPoints = []
        self.sketchUndo = []
        self.tmpSketchPoints = []
        self.tmpSketchUndo = []
        self.modelMode = "sketch"
    elif self.modelMode == "sketch":
        if (50 <= y <= 450):
            self.sketchPoints.append((x,y))
            self.sketchUndo = []
        if (710 <= x <= 780) and (10 <= y <= 40):
            if len(self.sketchPoints) >= 3:
                verts = calculateVerts(self.sketchPoints, 2)
                edges = calculateEdges(verts)
                self.curModel = Model(self.width, self.height, self._keys, verts, edges)
                self.modelMode = "view"
            #     self.findDepth = True
            #     while not ( <= x <= ) and 
            #     verts = calculateVerts(self.sketchPoints)
            #     edges = calculateEdges(verts)
            # else:
            #     self.sketchError = True

def createKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_m:
        self.sketchPoints = []
        self.sketchUndo = []
        self.curModel = None
        self.mode = "menu"
    if keyCode == pygame.K_h:
        self.mode = "help"
    if self.modelMode == "sketch":
        if keyCode == pygame.K_u:
            if (len(self.sketchPoints) == 0 and len(self.sketchUndo) == 0 and
                len(self.tmpSketchPoints) > 0):
                self.sketchPoints = self.tmpSketchPoints
                self.sketchUndo = self.tmpSketchUndo
                self.tmpSketchPoints = []
                self.sketchUndo = []
            elif len(self.sketchPoints) > 0:
                self.sketchUndo.append(self.sketchPoints.pop())
        if keyCode == pygame.K_r and len(self.sketchUndo) > 0:
            self.sketchPoints.append(self.sketchUndo.pop())
        if keyCode == pygame.K_c:
            self.tmpSketchPoints = self.sketchPoints
            self.tmpSketchUndo = self.sketchUndo
            self.sketchPoints = []
            self.sketchUndo = []

def createTimerFired(self, dt):
    if self.modelMode == "view" and not self.curModel == None:
        self.curModel.timerFired(dt)

def createRedrawAll(self, screen):
    drawOptions(self, screen)
    self.bgColor = (178, 0, 158)
    if self.modelMode == "sketch" and self.sketchError == False:
        for point in self.sketchPoints:
            pygame.draw.circle(screen, (0, 0, 0), point, 5)
        if len(self.sketchPoints) >= 3:
            pygame.draw.polygon(screen, (0, 0, 0), self.sketchPoints, 2)
    if self.modelMode == "view" and not self.curModel == None:
        self.curModel.redrawAll(screen)
    pygame.display.update((0, 50, 800, 400))

def drawOptions(self, screen):
    pygame.draw.rect(screen, (217, 224, 247), (0, 0, 800, 50))
    pygame.draw.rect(screen, (255, 0, 0), (20,10,70,30)) #sketch button
    if self.modelMode == "sketch":
        pygame.draw.rect(screen, (0, 255, 0), (710,10,70,30)) #finish sketch
    if self.sketchError == True:
        pygame.draw.rect(screen, (217, 224, 247), (150, 150, 500, 200))
    if self.findDepth == True:
        pygame.draw.rect(screen, (217, 224, 247), (150, 150, 500, 200))
        pygame.draw.rect(screen, (255, 255, 255), (150, 150, 500, 200))
        pygame.draw.rect(screen, (255, 255, 255), (150, 150, 500, 200))
        pygame.draw.polygon(screen, (255, 255, 255), (150, 150, 500, 200))
        pygame.draw.polygon(screen, (255, 255, 255), (150, 150, 500, 200))
    pygame.display.update((0, 0, 800, 50))
    