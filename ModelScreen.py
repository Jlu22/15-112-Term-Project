import pygame
from Model import Model
from Calculations import calculateVerts, calculateEdges
from Camera import Camera
from ModelScreenHelper import *
from SaveFiles import saveNew

def createInit(self):
    self.curModel = None
    self.modelMode = "view"
    self.sketchPoints = []
    self.sketchUndo = []
    self.tmpSketchPoints = []
    self.tmpSketchUndo = []
    self.sketchError = False
    self.findDepth = False
    self.findName = False
    self.curName = "Sample"
    self.nameError = False
    self.curDepth = 1.0
    self.isSaved = False
    self.displayName = None

def createMousePressed(self, x, y):
    if (self.modelMode == "view" and self.sketchError == False and 
        self.findDepth == False and (20 <= x <= 90) and (10 <= y <= 40)):
        self.sketchPoints = []
        self.sketchUndo = []
        self.tmpSketchPoints = []
        self.tmpSketchUndo = []
        self.modelMode = "sketch" #press sketch buttom
        self.curDepth = 1.0
        self.isSaved = False
        self.displayName = None
    elif (self.modelMode == "view" and not self.curModel == None and 
         (710 <= x <= 780) and (460 <= y <= 490) and self.isSaved == False):
        self.findName = True # click save
    elif self.modelMode == "sketch":
        if self.findDepth == True: # change depth
            changeDepth(self, x, y)
        elif (50 <= y <= 450) and self.sketchError == False: # add sketch point
            self.sketchPoints.append((x,y))
            self.sketchUndo = []
        elif ((710<= x <= 780) and (10 <= y <= 40) and self.sketchError == False
            and self.findDepth == False): # click finish sketch
            if len(self.sketchPoints) >= 3:
                self.findDepth = True
            else:
                self.sketchError = True

def createKeyPressed(self, keyCode, modifier):
    if (keyCode == pygame.K_m and self.findDepth == False and 
        self.sketchError == False and self.findName == False):
        self.sketchPoints = []
        self.sketchUndo = []
        self.curModel = None
        self.mode = "menu"
        self.isSaved = False
        self.displayName =  None
    if keyCode == pygame.K_h and self.findName == False:
        self.mode = "help"
    if self.modelMode == "sketch":
        sketchKeyPressed(self, keyCode, modifier)
    if self.modelMode == "view":
        viewKeyPressed(self, keyCode, modifier)

def viewKeyPressed(self, keyCode, modifier):
    if not self.curModel == None and keyCode == pygame.K_SPACE:
        self.curModel.camera = Camera((0, 0, -5))
    elif keyCode == pygame.K_RETURN:
        if self.nameError == True:
            self.nameError = False
        elif self.findName == True:
            if 1 <= len(self.curName) <= 15:
                self.findName = False
                verts = calculateVerts(self.sketchPoints, self.curDepth)
                edges = calculateEdges(verts)
                saveNew(self, verts, edges)
                self.displayName = self.curName
                self.curName = "Sample"
                self.isSaved = True
            else:
                self.nameError = True
    if self.findName == True and self.nameError == False: # type in name
        if keyCode == pygame.K_BACKSPACE and len(self.curName) > 0:
            self.curName = self.curName[:-1]
        elif (40 <= keyCode <= 126) and len(self.curName) < 10:
            if modifier & pygame.KMOD_SHIFT:
                self.curName += chr(keyCode).upper()
            else:
                self.curName += chr(keyCode)

def sketchKeyPressed(self, keyCode, modifier):
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
    if keyCode == pygame.K_RETURN:
        if self.sketchError == True:
            self.sketchError = False
        if self.findDepth == True:
            self.findDepth = False
            verts = calculateVerts(self.sketchPoints, self.curDepth)
            edges = calculateEdges(verts)
            self.curModel = Model(self.width, self.height, self._keys, 
                                    verts, edges)
            self.modelMode = "view"

def createTimerFired(self, dt):
    if self.modelMode == "view" and not self.curModel == None:
        self.curModel.timerFired(dt)

def createRedrawAll(self, screen):
    #print("name", self.findName)
    drawOptions(self, screen)
    self.bgColor = (178, 0, 158)
    if (self.modelMode == "sketch" and self.sketchError == False and 
        self.findDepth == False):
        for point in self.sketchPoints:
            pygame.draw.circle(screen, (0, 0, 0), point, 5)
        if len(self.sketchPoints) >= 3:
            pygame.draw.polygon(screen, (0, 0, 0), self.sketchPoints, 2)
    elif (self.modelMode == "view" and not self.curModel == None and 
          self.findName == False):
        self.curModel.redrawAll(screen)
    elif self.findDepth == True:
        depthDraw(self, screen)
    elif self.sketchError == True:
        pygame.draw.rect(screen, (217, 224, 247), (150, 150, 500, 200))
        font = pygame.font.SysFont("calibri", 25)
        message = font.render("Sketch must have at least three points", True,
                              (255, 0, 0))
        message2 = font.render("Press enter to continue", True, (255, 0, 0))
        screen.blit(message, (210, 220))
        screen.blit(message2, (270, 260))
    elif self.findName == True:
        if self.nameError == True:
            pygame.draw.rect(screen, (217, 224, 247), (150, 150, 500, 200))
            font = pygame.font.SysFont("calibri", 25)
            message = font.render("Name must be between 1 and 10 characters", 
                                    True,(255, 0, 0))
            message2 = font.render("Press enter to continue", True, (255, 0, 0))
            screen.blit(message, (175, 220))
            screen.blit(message2, (270, 260))
        else:
            nameDraw(self, screen)
        
    pygame.display.update((0, 50, 800, 400))