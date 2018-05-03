import pygame

def changeDepth(self, x, y): # mousepress buttons to change depth
    if ((217 <= x <= 247) and ((-2/3)*x+415 <= y <= (2/3)*x+125) and 
        self.curDepth > 0.1):
        self.curDepth -= 1
        if self.curDepth < 0.1:
            self.curDepth += 1
    elif ((553 <= x <= 583) and ((2/3)*x-119 <= y <= (-2/3)*x+659) and 
        self.curDepth < 10):
        self.curDepth += 1
        if self.curDepth > 10:
            self.curDepth -= 1
    elif ((169 <= x <= 194) and ((-2/3)*x+384 <= y <= (2/3)*x+156) and
        self.curDepth > 0.1):
        self.curDepth -= 0.1
        if self.curDepth < 0.1:
            self.curDepth += 0.1
    elif ((606 <= x <= 631) and ((2/3)*x-149 <= y <= (-2/3)*x+689) and 
        self.curDepth < 10):
        self.curDepth += 0.1
        if self.curDepth > 10:
            self.curDepth -= 0.1

def depthDraw(self, screen): # depth pop-up
    pygame.draw.rect(screen, (217, 224, 247), (150, 150, 500, 200))
    pygame.draw.rect(screen, (255, 255, 255), (275, 220, 250, 100)) #nums
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

def nameDraw(self,screen): # name pop-up
    pygame.draw.rect(screen, (217, 224, 247), (150, 150, 500, 200))
    pygame.draw.rect(screen, (255, 255, 255), (200, 220, 400, 90))
    
    lfont = pygame.font.SysFont("calibri", 40)
    sfont = pygame.font.SysFont("calibri", 15)
    title = lfont.render("Name your creation!", True, (0, 0, 0))
    message = sfont.render("Keep it within 10 characters", True, (0, 0, 0))
    message2 = sfont.render("Press enter to continue", True, (0, 0, 0))
    screen.blit(title, (400 - title.get_rect().width // 2, 170))
    screen.blit(message, (400 - message.get_rect().width // 2, 315))
    screen.blit(message2, (400 - message2.get_rect().width // 2, 330))
    
    wordFont = pygame.font.SysFont("calibri", 45)
    name = wordFont.render(self.curName, True, (0, 255, 0))
    width = name.get_rect().width
    screen.blit(name, (400 - width//2, 245))

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
    if (self.modelMode == "view" and not self.curModel == None and 
        self.isSaved == False and self.findName == False):
        pygame.draw.rect(screen, (0, 0, 255), (710,460,70,30)) # save model
        save = optionFont.render("Save", True, (0, 0, 0))
        screen.blit(save, (725, 465))
    if not self.displayName == None: # displays name of saved model
        font = pygame.font.SysFont("calibri", 40)
        name = font.render(self.displayName, True, (0, 0, 0))
        screen.blit(name, (400 - name.get_rect().width // 2, 10))
    pygame.display.update((0, 0, 800, 50))
    pygame.display.update((0, 450, 800, 50))