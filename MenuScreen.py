# File contains functions used for the main menu
# Button presses (keypressed) and text displays

import pygame

def menuInit(self):
    pass

def menuMousePressed(self, x, y):
    if (170 <= x <= 380) and (280 <= y <= 340):
        self.mode = "create"
    elif (430 <= x <= 650) and (280 <= y <= 340):
        self.mode = "assem"
    elif (170 <= x <= 380) and (360 <= y <= 420):
        self.mode = "help"
    elif (430 <= x <= 650) and (360 <= y <= 420):
        self.mode = "save"

def menuKeyPressed(self, keyCode, modifier):
    pass

def menuTimerFired(self, dt):
    pass

def menuRedrawAll(self, screen):
    lFont = pygame.font.SysFont("calibri", 60)
    sFont = pygame.font.SysFont("calibri", 40)
    title = lFont.render("PyCAD Mini", True, (0, 0, 0))
    create = sFont.render("Create", True, (0, 0, 0))
    assem = sFont.render("Assemble", True, (0, 0, 0))
    help = sFont.render("Help", True, (0, 0, 0))
    saved = sFont.render("Saved", True, (0, 0, 0))
    
    self.bgColor = (217, 224, 247)
    pygame.draw.rect(screen, (255, 0, 0), (170, 280, 210, 60))
    pygame.draw.rect(screen, (0, 0, 255), (430, 280, 210, 60))
    pygame.draw.rect(screen, (0, 255, 100), (170, 360, 210, 60))
    pygame.draw.rect(screen, (100, 100, 0), (430, 360, 210, 60))
    
    screen.blit(title, (self.width//2 - 137, self.height//4))
    screen.blit(create, (225, 295))
    screen.blit(assem, (460, 295))
    screen.blit(help, (234, 375))
    screen.blit(saved, (490, 375))
    
    pygame.display.flip()