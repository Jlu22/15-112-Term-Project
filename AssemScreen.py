# This file contains all of the functions used in the Assemble mode.
# "Import" button and preview of models being inputted is controlled here
# When import is pressed, gives preview of saved models, which can be toggled
# through before choosing which to put into assembly

import pygame
from Model import Model

def assemInit(self):
    self.assemList = []
    self.tmpModel = 0
    self.preview = None
    self.assemMode = "view"

def assemMousePressed(self, x, y):
    if (20 <= x <= 90) and (10 <= y <= 40): # click import button
        self.assemMode = "import"
        verts = self.saved[self.tmpModel][1]
        edges = self.saved[self.tmpModel][2]
        self.preview = Model(self.width, self.height, self._keys, verts, edges)
    elif self.assemMode == "import": # change imported model
        if ((45 <= x <= 75) and (-0.5*x+497 <= y <= 0.5*x+453) and 
             self.tmpModel > 0):
            self.tmpModel -= 1
        elif ((725 <= x <= 755) and (0.5*x+97 <= y <= -0.5*x+853) and
               self.tmpModel < len(self.saved) -1):
            self.tmpModel += 1
        verts = self.saved[self.tmpModel][1]
        edges = self.saved[self.tmpModel][2]
        self.preview = Model(self.width, self.height, self._keys, verts, edges)

def assemKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_n and self.assemMode == "view":
        self.assemMode = "import"
    if keyCode == pygame.K_m:
        self.assemList = []
        self.mode = "menu"
        self.assemMode = "view"
    if keyCode == pygame.K_h:
        self.mode = "help"
        self.helpScreen = 4
    if keyCode == pygame.K_u and len(self.assemList) > 0:
        self.assemList.pop()
        
    if self.assemMode == "import": # change imported model
        if keyCode == pygame.K_LEFT and self.tmpModel > 0:
            self.tmpModel -= 1
        elif keyCode == pygame.K_RIGHT and self.tmpModel < len(self.saved) - 1:
            self.tmpModel += 1
        verts = self.saved[self.tmpModel][1]
        edges = self.saved[self.tmpModel][2]
        self.preview = Model(self.width, self.height, self._keys, verts, edges)
        
        if keyCode == pygame.K_RETURN:
            self.assemList.append(self.preview)
            self.preview = None
            self.assemMode = "view"

def assemTimerFired(self, dt):
    if self.assemMode == "view":
        for model in self.assemList:
            model.timerFired(dt)

def assemRedrawAll(self, screen):
    assemOptions(self, screen)
    self.bgColor = (245,245,220)
    for model in self.assemList:
        model.redrawAll(screen)
    
    if self.assemMode == "import":
       self.preview.redrawAll(screen)
    
    pygame.display.update((0, 50, 800, 400)) # updates mid screen

def assemOptions(self, screen):
    pygame.draw.rect(screen, (217, 224, 247), (0, 0, 800, 50))
    pygame.draw.rect(screen, (217, 224, 247), (0, 450, 800, 50))
    
    sfont = pygame.font.SysFont("calibri", 15)
    mfont = pygame.font.SysFont("calibri", 20)
    lfont = pygame.font.SysFont("calibri", 40)
    pygame.draw.rect(screen, (200, 0, 0), (20,10,70,30)) # import button
    sketch = mfont.render("Import", True, (0, 0, 0))
    screen.blit(sketch, (28, 18))
    
    if self.assemMode == "import":
        message = lfont.render("Select model to import", True, (0, 0, 0))
        screen.blit(message, (400 - message.get_rect().width // 2, 10))
        message2 = sfont.render("Press enter to continue", True, (0, 0, 0))
        screen.blit(message2, (400 - message2.get_rect().width // 2, 480))
        name = mfont.render(self.saved[self.tmpModel][0], True, (0, 0, 0))
        screen.blit(name, (400 - name.get_rect().width // 2, 460))
        
        pygame.draw.polygon(screen, (200, 0, 0),[(725,460),(755,475),(725,490)])
        pygame.draw.polygon(screen, (200, 0, 0), [(45,475),(75,460),(75,490)])
    
    pygame.display.update((0, 0, 800, 50)) # updates upper banner
    pygame.display.update((0, 450, 800, 50)) # lower banner