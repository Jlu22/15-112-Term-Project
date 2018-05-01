import pygame

def saveInit(self):
    pass

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
    pygame.draw.rect(screen, (0, 0, 255), (430, 280, 210, 60))
    pygame.draw.rect(screen, (0, 255, 100), (170, 360, 210, 60))
    
    pygame.display.flip()
