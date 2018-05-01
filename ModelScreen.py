import pygame
from Model import Model
from Calculations import calculateVerts, calculateEdges
from Camera import Camera

def createInit(self):
    self.curModel = None
    self.modelMode = "view"
    self.sketchPoints = []
    self.sketchUndo = []
    self.tmpSketchPoints = []
    self.tmpSketchUndo = []
    self.sketchError = False
    self.findDepth = False
    self.createModel = False
    self.curDepth = 1.0

def createMousePressed(self, x, y):
    if (self.modelMode == "view" and self.sketchError == False and 
        self.findDepth == False and (20 <= x <= 90) and (10 <= y <= 40)):
        self.sketchPoints = []
        self.sketchUndo = []
        self.tmpSketchPoints = []
        self.tmpSketchUndo = []
        self.modelMode = "sketch"
    elif self.modelMode == "sketch":
        if self.findDepth == True: # change depth
            changeDepth(self, x, y)
        elif (50 <= y <= 450) and self.sketchError == False: # add sketch point
            self.sketchPoints.append((x,y))
            self.sketchUndo = []
        elif ((710 <= x <= 780) and (10 <= y <= 40) and self.sketchError == False
            and self.findDepth == False): # click finish sketch
            if len(self.sketchPoints) >= 3:
                self.findDepth = True
                # self.saved += str(self.curModel)
                # print(self.saved)
            else:
                self.sketchError = True

def changeDepth(self, x, y):
    if ((207 <= x <= 257) and (240 <= y <= 300) and 
        self.curDepth > 0.1):
        self.curDepth -= 1
        if self.curDepth < 0.1:
            self.curDepth += 1
    elif ((543 <= x <= 593) and (240 <= y <= 300) and 
        self.curDepth < 10):
        self.curDepth += 1
        if self.curDepth > 10:
            self.curDepth -= 1
    elif ((164 <= x <= 199) and (250 <= y <= 290) and
        self.curDepth > 0.1):
        self.curDepth -= 0.1
        if self.curDepth < 0.1:
            self.curDepth += 0.1
    elif ((601 <= x <= 636) and (250 <= y <= 290) and 
        self.curDepth < 10):
        self.curDepth += 0.1
        if self.curDepth > 10:
            self.curDepth -= 0.1

def createKeyPressed(self, keyCode, modifier):
    if (keyCode == pygame.K_m and self.findDepth == False and 
        self.sketchError == False):
        self.sketchPoints = []
        self.sketchUndo = []
        self.curModel = None
        self.mode = "menu"
    if keyCode == pygame.K_h:
        self.mode = "help"
    if self.modelMode == "sketch":
        sketchKeyPressed(self, keyCode, modifier)
    if self.modelMode == "view" and not self.curModel == None:
        if keyCode == pygame.K_SPACE:
            self.curModel.camera = Camera((0, 0, -5))
        

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
        elif self.findDepth == True:
            self.findDepth = False
            self.createModel = True

def createTimerFired(self, dt):
    if self.createModel == True:
        verts = calculateVerts(self.sketchPoints, self.curDepth)
        edges = calculateEdges(verts)
        print(verts)
        print(edges)
        self.curModel = Model(self.width, self.height, self._keys, 
                                verts, edges)
        self.createModel = False
        self.modelMode = "view"
        self.curDepth = 1.0
    if self.modelMode == "view" and not self.curModel == None:
        self.curModel.timerFired(dt)

def createRedrawAll(self, screen):
    drawOptions(self, screen)
    self.bgColor = (178, 0, 158)
    if (self.modelMode == "sketch" and self.sketchError == False and 
        self.findDepth == False):
        for point in self.sketchPoints:
            pygame.draw.circle(screen, (0, 0, 0), point, 5)
        if len(self.sketchPoints) >= 3:
            pygame.draw.polygon(screen, (0, 0, 0), self.sketchPoints, 2)
    elif self.modelMode == "view" and not self.curModel == None:
        self.curModel.redrawAll(screen)
    pygame.display.update((0, 50, 800, 400))

def drawOptions(self, screen):
    pygame.draw.rect(screen, (217, 224, 247), (0, 0, 800, 50))
    pygame.draw.rect(screen, (217, 224, 247), (0, 450, 800, 50))
    optionFont = pygame.font.SysFont("calibri", 20)
    if self.sketchError == False and self.findDepth == False:
        pygame.draw.rect(screen, (255, 0, 0), (20,10,70,30)) #sketch button
        sketch = optionFont.render("Sketch", True, (0, 0, 0))
        screen.blit(sketch, (29, 18))
    if (self.modelMode == "sketch" and self.sketchError == False and 
        self.findDepth == False):
        pygame.draw.rect(screen, (0, 255, 0), (710,10,70,30)) #finish sketch
        finish = optionFont.render("Extrude", True, (0, 0, 0))
        screen.blit(finish, (712, 18))
    if self.modelMode == "view" and not self.curModel == None:
        pygame.draw.rect(screen, (0, 0, 255), (710,460,70,30)) # save model
        save = optionFont.render("Save", True, (0, 0, 0))
        screen.blit(save, (725, 465))
    if self.sketchError == True:
        pygame.draw.rect(screen, (217, 224, 247), (150, 150, 500, 200))
        font = pygame.font.SysFont("calibri", 25)
        message = font.render("Sketch must have at least three points", True,
                              (255, 0, 0))
        message2 = font.render("Press enter to continue", True, (255, 0, 0))
        screen.blit(message, (210, 220))
        screen.blit(message2, (270, 260))
    if self.findDepth == True:
        depthDraw(self, screen)
    pygame.display.update((0, 0, 800, 50))
    pygame.display.update((0, 450, 800, 50))

def depthDraw(self, screen):
    pygame.draw.rect(screen, (217, 224, 247), (150, 150, 500, 200))
    pygame.draw.rect(screen, (255, 255, 255), (275, 220, 250, 100)) #nums
    pygame.draw.rect(screen, (255, 255, 255), (207, 240, 50, 60)) #l step
    pygame.draw.rect(screen, (255, 255, 255), (543, 240, 50, 60))
    pygame.draw.rect(screen, (255, 255, 255), (164, 250, 35, 40)) #s step
    pygame.draw.rect(screen, (255, 255, 255), (601, 250, 35, 40))
    pygame.draw.polygon(screen, (0, 0, 255),[(217,270),(247,250),(247,290)])
    pygame.draw.polygon(screen, (0, 0, 255),[(553,250),(553,290),(583,270)])
    pygame.draw.polygon(screen, (0, 0, 255),[(169,270),(194,255),(194,285)])
    pygame.draw.polygon(screen, (0, 0, 255),[(606,255),(606,285),(631,270)])
    
    font = pygame.font.SysFont("calibri", 40)
    sfont = pygame.font.SysFont("calibri", 20)
    message = font.render("Select Depth", True, (255, 0, 0))
    message2 = sfont.render("Press enter to continue", True, (255, 0, 0))
    screen.blit(message, (300, 170))
    screen.blit(message2, (305, 325))
    
    numFont = pygame.font.SysFont("calibri", 60)
    depth = numFont.render("%0.1f" %self.curDepth, True, (0, 255, 0))
    width = depth.get_rect().width
    screen.blit(depth, (400 - width//2, 245))