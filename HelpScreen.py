import pygame

def helpInit(self):
    self.helpScreen = 1

def helpMousePressed(self, x, y):
    if (730 <= x <= 790) and (430 <= y <= 490) and self.helpScreen < 4:
        self.helpScreen += 1
    elif (660 <= x <= 720) and (430 <= y <= 490) and self.helpScreen > 1:
        self.helpScreen -= 1

def helpKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_RIGHT and self.helpScreen < 4:
        self.helpScreen += 1
    if keyCode == pygame.K_LEFT and self.helpScreen > 1:
        self.helpScreen -= 1
    if keyCode == pygame.K_m:
        self.helpScreen = 1
        self.mode = "menu"

def helpRedrawAll(self, screen):
    self.bgColor = (217, 224, 247)
    
    page1Text1 = "Welcome to PyCAD!"
    page1Text2 = "Press 'm' to return to the menu"
    page1Text3 = "At any time you can press this to return to help"
    page1Text4 ="Or press the left and right arrows to get help for other modes"
    
    pygame.draw.rect(screen, (255, 255, 255), (730,430,60,60))
    pygame.draw.rect(screen, (255, 255, 255), (660,430,60,60))
    pygame.draw.polygon(screen, (0, 0, 255), [(740, 440),(780, 460),
                        (740,480)])
    pygame.draw.polygon(screen, (0, 0, 255), [(670, 460),(710,440),
                        (710,480)])
    font = pygame.font.SysFont("calibri", 30)
    if self.helpScreen == 1:
        textP11 = font.render(page1Text1, True, (0, 128, 0))
        textP12 = font.render(page1Text2, True, (0, 128, 0))
        textP13 = font.render(page1Text3, True, (0, 128, 0))
        textP14 = font.render(page1Text4, True, (0, 128, 0))
        screen.blit(textP11, (30, 150))
        screen.blit(textP12, (30, 200))
        screen.blit(textP13, (30, 250))
        screen.blit(textP14, (30, 300))
        
    elif self.helpScreen == 2:
        textP21 = font.render("Page 2", True, (0, 128, 0))
        screen.blit(textP21, (30, 250))
    elif self.helpScreen == 3:
        textP31 = font.render("Page 3", True, (0, 128, 0))
        screen.blit(textP31, (30, 250))
    elif self.helpScreen == 4:
        textP41 = font.render("Page 4", True, (0, 128, 0))
        screen.blit(textP41, (30, 250))
    else:
        text = font.render("Too far!!", True, (0, 128, 0))
        screen.blit(text, (30, 250))
    pygame.display.flip()