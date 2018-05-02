import pygame
from SaveFiles import checkSaved
from Model import Model

def saveInit(self):
    self.saved = []
    checkSaved(self)
    self.curSave = -1
    self.savePage = 1
    self.maxPages = 2
    calculateMax(self)
    print("page",self.maxPages)

def calculateMax(self):
    numModels = len(self.saved)
    if numModels % 6 == 0:
        self.maxPages = numModels//6
    else:
        self.maxPages = numModels//6 +1

def saveMousePressed(self, x, y):
    # self.modelMode = "view"
    # self.mode = "create"
    if ((725 <= x <= 775) and ((0.5*x - 137.5) <= y <= (-0.5*x + 637.5)) and
        self.savePage < self.maxPages):
        self.savePage += 1
    elif ((25 <= x <= 75) and ((-0.5*x + 262.5) <= y <= (0.5*x + 237.5)) and
        self.savePage > 1):
        self.savePage -= 1
    
    boxNum = -1
    if (100 <= x <= 280) and (100 <= y <= 235):
        boxNum = 0
    elif (310 <= x <= 490) and (100 <= y <= 235):
        boxNum = 1
    elif (520 <= x <= 700) and (100 <= y <= 235):
        boxNum = 2
    elif (100 <= x <= 280) and (265 <= y <= 400):
        boxNum = 3
    elif (310 <= x <= 490) and (265 <= y <= 400):
        boxNum = 4
    elif (520 <= x <= 700) and (265 <= y <= 400):
        boxNum = 5
    
    if boxNum != -1:
        modelIndex = boxNum + (self.savePage - 1) * 6
        if modelIndex < len(self.saved):
            verts = self.saved[modelIndex][1]
            edges = self.saved[modelIndex][2]
            self.curModel = Model(self.width, self.height, self._keys, verts, edges)
            self.modelMode = "view"
            self.mode = "create"
            self.savePage = 1

def saveKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_m:
        self.mode = "menu"
        self.savePage = 1
    if keyCode == pygame.K_h:
        self.mode = "help"
    if keyCode == pygame.K_RIGHT and self.savePage < self.maxPages:
        self.savePage += 1
    if keyCode == pygame.K_LEFT and self.savePage > 1:
        self.savePage -= 1

def saveTimerFired(self, dt):
    pass

def saveRedrawAll(self, screen):
    calculateMax(self)
    self.bgColor = (217, 224, 247)
    
    if self.savePage != self.maxPages:
        pygame.draw.polygon(screen, (200, 0, 0),[(725,225),(775,250),(725,275)])
    if self.savePage != 1:
        pygame.draw.polygon(screen, (200, 0, 0), [(25,250),(75,225),(75,275)])
    
    for num in range(len(self.saved)):
        #print(self.saved[num][0], num)
        start = (self.savePage - 1) * 6
        if start <= num <= start + 5:
            name = self.saved[num][0]
            verts = self.saved[num][1]
            edges = self.saved[num][2]
            
            font = pygame.font.SysFont("calibri", 25)
            label = font.render(name, True, (255, 255, 255))
            width = label.get_rect().width
            
            if num % 6 == 0: # box 0
                pygame.draw.rect(screen, (200, 0, 0), (100, 100, 180, 135))
                screen.blit(label, (190 - width//2, 200))
            elif num % 6 == 1: # box 1
                pygame.draw.rect(screen, (200, 0, 0), (310, 100, 180, 135))
                screen.blit(label, (400 - width//2, 200))
            elif num % 6 == 2: # box 2
                pygame.draw.rect(screen, (200, 0, 0), (520, 100, 180, 135))
                screen.blit(label, (610 - width//2, 200))
            elif num % 6 == 3: # box 3
                pygame.draw.rect(screen, (200, 0, 0), (100, 265, 180, 135))
                screen.blit(label, (190 - width//2, 365))
            elif num % 6 == 4: # box 4
                pygame.draw.rect(screen, (200, 0, 0), (310, 265, 180, 135))
                screen.blit(label, (400 - width//2, 365))
            elif num % 6 == 5: # box 5
                pygame.draw.rect(screen, (200, 0, 0), (520, 265, 180, 135))
                screen.blit(label, (610 - width//2, 365))
    
    pygame.display.flip()