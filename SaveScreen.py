import pygame

def saveInit(self):
    self.saved = []
    self.curSave = -1
    self.savePage = 1

def saveMousePressed(self, x, y):
    self.modelMode = "view"
    self.mode = "create"

def saveKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_m:
        self.mode = "menu"
    if keyCode == pygame.K_h:
        self.mode = "help"

def saveTimerFired(self, dt):
    pass

def saveRedrawAll(self, screen):
    self.bgColor = (217, 224, 247)
    
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
            
            if num % 6 == 0:
                pygame.draw.rect(screen, (200, 0, 0), (100, 100, 180, 135))
                screen.blit(label, (190 - width//2, 200))
            elif num % 6 == 1:
                pygame.draw.rect(screen, (200, 0, 0), (310, 100, 180, 135))
                screen.blit(label, (400 - width//2, 200))
            elif num % 6 == 2:
                pygame.draw.rect(screen, (200, 0, 0), (520, 100, 180, 135))
                screen.blit(label, (610 - width//2, 200))
            elif num % 6 == 3:
                pygame.draw.rect(screen, (200, 0, 0), (100, 265, 180, 135))
                screen.blit(label, (190 - width//2, 365))
            elif num % 6 == 4:
                pygame.draw.rect(screen, (200, 0, 0), (310, 265, 180, 135))
                screen.blit(label, (400 - width//2, 365))
            elif num % 6 == 5:
                pygame.draw.rect(screen, (200, 0, 0), (520, 265, 180, 135))
                screen.blit(label, (610 - width//2, 365))
    
    pygame.display.flip()