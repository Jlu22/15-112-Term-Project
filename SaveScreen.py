import pygame

def saveInit(self):
    self.saved = ""

def saveMousePressed(self, x, y):
    print(self.mode)
    self.modelMode = "view"
    self.mode = "create"
    print(self.mode)

def saveKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_m:
        self.mode = "menu"
    if keyCode == pygame.K_h:
        self.mode = "help"

def saveTimerFired(self, dt):
    pass

def saveRedrawAll(self, screen):
    self.bgColor = (217, 224, 247)
    
    
    pygame.display.flip()
