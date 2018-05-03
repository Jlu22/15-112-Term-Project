import pygame

def helpInit(self):
    self.helpScreen = 1

def helpMousePressed(self, x, y):
    if (730 <= x <= 790) and (430 <= y <= 490) and self.helpScreen < 5:
        self.helpScreen += 1
    elif (660 <= x <= 720) and (430 <= y <= 490) and self.helpScreen > 1:
        self.helpScreen -= 1

def helpKeyPressed(self, keyCode, modifier):
    if keyCode == pygame.K_RIGHT and self.helpScreen < 5:
        self.helpScreen += 1
    if keyCode == pygame.K_LEFT and self.helpScreen > 1:
        self.helpScreen -= 1
    if keyCode == pygame.K_m:
        self.helpScreen = 1
        self.mode = "menu"

def helpRedrawAll(self, screen):
    self.bgColor = (217, 224, 247)
    font = pygame.font.SysFont("calibri", 25)
    
    if self.helpScreen == 1:
        helpPage1(self, screen)
    elif self.helpScreen == 2:
        helpPage2(self, screen)
    elif self.helpScreen == 3:
        helpPage3(self, screen)
    elif self.helpScreen == 4:
        helpPage4(self, screen)
    elif self.helpScreen == 5:
        helpPage5(self, screen)
    else:
        text = font.render("Too far!!", True, (0, 128, 0))
        screen.blit(text, (30, 250))
    
    if self.helpScreen != 5:
        pygame.draw.rect(screen, (255, 255, 255), (730,430,60,60)) # right arrow
        pygame.draw.polygon(screen, (0, 0, 255), [(740, 440),(780, 460),
                            (740,480)])
    
    if self.helpScreen != 1:
        pygame.draw.rect(screen, (255, 255, 255), (660,430,60,60)) # left arrow
        pygame.draw.polygon(screen, (0, 0, 255), [(670, 460),(710,440),
                            (710,480)])
    
    pygame.display.flip()
    
def helpPage1(self, screen):
    titleFont = pygame.font.SysFont("calibri", 60)
    font = pygame.font.SysFont("calibri", 25)
    
    page1Text1 = "Welcome to PyCAD!"
    page1Text2 = "Press 'm' to return to the menu"
    page1Text3 = "At any time you can press 'h' to return to help"
    page1Text4 ="Or press the left and right arrows to get help for other modes"
    
    textP11 = titleFont.render(page1Text1, True, (200, 0, 0))
    textP12 = font.render(page1Text2, True, (200, 0, 0))
    textP13 = font.render(page1Text3, True, (200, 0, 0))
    textP14 = font.render(page1Text4, True, (200, 0, 0))
    screen.blit(textP11, (400 - textP11.get_rect().width //2, 100))
    screen.blit(textP12, (400 - textP12.get_rect().width //2, 240))
    screen.blit(textP13, (400 - textP13.get_rect().width //2, 270))
    screen.blit(textP14, (400 - textP14.get_rect().width //2, 360))
    
def helpPage2(self, screen):
    titleFont = pygame.font.SysFont("calibri", 40)
    font = pygame.font.SysFont("calibri", 25)
    
    page2Text1 = "Create Mode"
    page2Text2 = "Draw your own shapes to create a 3D model!"
    page2Text3 = "To start, select the top left button 'sketch'"
    page2Text4 = "Click on the screen to create points"
    page2Text5 = "Press 'u' to undo, 'r' to redo, or 'c' to clear"
    page2Text6 = "When you are finished, select the top right button 'extrude'"
    page2Text7 = "You will be prompted to select a depth"
    page2Text8 = "Use the arrows to change the value, which ranges from 0.1-10"
    page2Text9 = "Keep in mind that ~200 pixels is 1 unit"
    
    textP21 = titleFont.render(page2Text1, True, (0, 128, 0))
    textP22 = font.render(page2Text2, True, (0, 128, 0))
    textP23 = font.render(page2Text3, True, (0, 128, 0))
    textP24 = font.render(page2Text4, True, (0, 128, 0))
    textP25 = font.render(page2Text5, True, (0, 128, 0))
    textP26 = font.render(page2Text6, True, (0, 128, 0))
    textP27 = font.render(page2Text7, True, (0, 128, 0))
    textP28 = font.render(page2Text8, True, (0, 128, 0))
    textP29 = font.render(page2Text9, True, (0, 128, 0))
    
    screen.blit(textP21, (400 - textP21.get_rect().width //2, 50))
    screen.blit(textP22, (400 - textP22.get_rect().width //2, 90))
    screen.blit(textP23, (400 - textP23.get_rect().width //2, 180))
    screen.blit(textP24, (400 - textP24.get_rect().width //2, 210))
    screen.blit(textP25, (400 - textP25.get_rect().width //2, 240))
    screen.blit(textP26, (400 - textP26.get_rect().width //2, 300))
    screen.blit(textP27, (400 - textP27.get_rect().width //2, 330))
    screen.blit(textP28, (400 - textP28.get_rect().width //2, 360))
    screen.blit(textP29, (400 - textP29.get_rect().width //2, 390))
    
def helpPage3(self, screen):
    font = pygame.font.SysFont("calibri", 25)
    
    page3Text1 = "After you enter the depth, you should see your new model!"
    page3Text9 = "Move it around using the arrow keys"
    page3Text10 = "If it goes off the screen, press space to center it again"
    page3Text2 = "If you want to save it, select the bottom right button 'save'"
    page3Text3 = "You will be prompted to input a name for your model"
    page3Text4 = "Go ahead and type it in! Keep it within 10 characters."
    page3Text5 = "When you finish, you should see the name at the top"
    page3Text6 = "If you go to the saved screen, you can view it again"
    page3Text7 = "Or you can even put it into an assembly!"
    page3Text8 = "Read on to learn how to do these things with your model"
    
    textP31 = font.render(page3Text1, True, (0, 128, 0))
    textP32 = font.render(page3Text2, True, (0, 128, 0))
    textP33 = font.render(page3Text3, True, (0, 128, 0))
    textP34 = font.render(page3Text4, True, (0, 128, 0))
    textP35 = font.render(page3Text5, True, (0, 128, 0))
    textP36 = font.render(page3Text6, True, (0, 128, 0))
    textP37 = font.render(page3Text7, True, (0, 128, 0))
    textP38 = font.render(page3Text8, True, (0, 128, 0))
    textP39 = font.render(page3Text9, True, (0, 128, 0))
    textP310 = font.render(page3Text10, True, (0, 128, 0))
    
    screen.blit(textP31, (400 - textP31.get_rect().width //2, 80))
    screen.blit(textP39, (400 - textP39.get_rect().width //2, 110))
    screen.blit(textP310, (400 - textP310.get_rect().width //2, 140))
    screen.blit(textP32, (400 - textP32.get_rect().width //2, 190))
    screen.blit(textP33, (400 - textP33.get_rect().width //2, 220))
    screen.blit(textP34, (400 - textP34.get_rect().width //2, 250))
    screen.blit(textP35, (400 - textP35.get_rect().width //2, 300))
    screen.blit(textP36, (400 - textP36.get_rect().width //2, 330))
    screen.blit(textP37, (400 - textP37.get_rect().width //2, 360))
    screen.blit(textP38, (400 - textP38.get_rect().width //2, 390))
    
def helpPage4(self, screen):
    titleFont = pygame.font.SysFont("calibri", 40)
    font = pygame.font.SysFont("calibri", 25)
    
    page4Text1 = "Assemble Mode"
    page4Text2 = "Put together the models you made!"
    page4Text3 = "Press 'n' or the top left button 'import' to place a model"
    page4Text4 = "Use the arrow keys to select a model to import"
    page4Text5 = "Move the models around using the arrow keys"
    page4Text6 = "Press 'i' to zoom in and 'o' to zoom out"
    
    textP41 = titleFont.render(page4Text1, True, (0, 0, 128))
    textP42 = font.render(page4Text2, True, (0, 0, 128))
    textP43 = font.render(page4Text3, True, (0, 0, 128))
    textP44 = font.render(page4Text4, True, (0, 0, 128))
    textP45 = font.render(page4Text5, True, (0, 0, 128))
    textP46 = font.render(page4Text6, True, (0, 0, 128))
    
    screen.blit(textP41, (400 - textP41.get_rect().width //2, 100))
    screen.blit(textP42, (400 - textP42.get_rect().width //2, 140))
    screen.blit(textP43, (400 - textP43.get_rect().width //2, 230))
    screen.blit(textP44, (400 - textP44.get_rect().width //2, 260))
    screen.blit(textP45, (400 - textP45.get_rect().width //2, 290))
    screen.blit(textP46, (400 - textP46.get_rect().width //2, 320))
    
def helpPage5(self, screen):
    titleFont = pygame.font.SysFont("calibri", 40)
    font = pygame.font.SysFont("calibri", 25)
    
    page5Text1 = "Saved Mode"
    page5Text2 = "This is where all your saved models go!"
    page5Text3 = "The name of the model is on each red button"
    page5Text4 = "Once you select a model, you can choose to view or delete it"
    page5Text5="You can't bring back deleted models, so think before you click!"
    page5Text6 = "Saved models remain even if the program is closed"
    
    textP51 = titleFont.render(page5Text1, True, (200, 0, 0))
    textP52 = font.render(page5Text2, True, (200, 0, 0))
    textP53 = font.render(page5Text3, True, (200, 0, 0))
    textP54 = font.render(page5Text4, True, (200, 0, 0))
    textP55 = font.render(page5Text5, True, (200, 0, 0))
    textP56 = font.render(page5Text6, True, (200, 0, 0))
    
    screen.blit(textP51, (400 - textP51.get_rect().width //2, 100))
    screen.blit(textP52, (400 - textP52.get_rect().width //2, 140))
    screen.blit(textP53, (400 - textP53.get_rect().width //2, 230))
    screen.blit(textP54, (400 - textP54.get_rect().width //2, 260))
    screen.blit(textP55, (400 - textP55.get_rect().width //2, 290))
    screen.blit(textP56, (400 - textP56.get_rect().width //2, 320))