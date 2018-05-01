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
    font = pygame.font.SysFont("calibri", 30)
    
    if self.helpScreen == 1:
        helpPage1(self, screen, font)
    elif self.helpScreen == 2:
        helpPage2(self, screen, font)
    elif self.helpScreen == 3:
        helpPage3(self, screen, font)
    elif self.helpScreen == 4:
        helpPage4(self, screen, font)
    else:
        text = font.render("Too far!!", True, (0, 128, 0))
        screen.blit(text, (30, 250))
    
    if self.helpScreen != 4:
        pygame.draw.rect(screen, (255, 255, 255), (730,430,60,60)) # right arrow
        pygame.draw.polygon(screen, (0, 0, 255), [(740, 440),(780, 460),
                            (740,480)])
    
    if self.helpScreen != 1:
        pygame.draw.rect(screen, (255, 255, 255), (660,430,60,60)) # left arrow
        pygame.draw.polygon(screen, (0, 0, 255), [(670, 460),(710,440),
                            (710,480)])
    
    pygame.display.flip()
    
def helpPage1(self, screen, font):
    page1Text1 = "Welcome to PyCAD!"
    page1Text2 = "Press 'm' to return to the menu"
    page1Text3 = "At any time you can press 'h' to return to help"
    page1Text4 ="Or press the left and right arrows to get help for other modes"
    
    textP11 = font.render(page1Text1, True, (0, 128, 0))
    textP12 = font.render(page1Text2, True, (0, 128, 0))
    textP13 = font.render(page1Text3, True, (0, 128, 0))
    textP14 = font.render(page1Text4, True, (0, 128, 0))
    screen.blit(textP11, (30, 150))
    screen.blit(textP12, (30, 200))
    screen.blit(textP13, (30, 250))
    screen.blit(textP14, (30, 300))
    
def helpPage2(self, screen, font):
    page2Text1 = "Create Mode"
    page2Text2 = "Select the top right red button to begin sketch"
    page2Text3 = "Click on the screen to create points"
    page2Text4 = "Press 'u' to undo and 'r' to redo"
    
    textP21 = font.render(page2Text1, True, (0, 128, 0))
    textP22 = font.render(page2Text2, True, (0, 128, 0))
    textP23 = font.render(page2Text3, True, (0, 128, 0))
    textP24 = font.render(page2Text4, True, (0, 128, 0))
    screen.blit(textP21, (30, 150))
    screen.blit(textP22, (30, 200))
    screen.blit(textP23, (30, 250))
    screen.blit(textP24, (30, 300))
    
def helpPage3(self, screen, font):
    page3Text1 = "Assemble Mode"
    page3Text2 = "Press 'n' to create new model"
    page3Text3 = "Press the arrow keys to move the camera"
    page3Text4 = "Press 'i' to zoom in and 'o' to zoom out"
    
    textP31 = font.render(page3Text1, True, (0, 128, 0))
    textP32 = font.render(page3Text2, True, (0, 128, 0))
    textP33 = font.render(page3Text3, True, (0, 128, 0))
    textP34 = font.render(page3Text4, True, (0, 128, 0))
    screen.blit(textP31, (30, 150))
    screen.blit(textP32, (30, 200))
    screen.blit(textP33, (30, 250))
    screen.blit(textP34, (30, 300))
    
def helpPage4(self, screen, font):
    textP41 = font.render("Page 4", True, (0, 128, 0))
    screen.blit(textP41, (30, 250))