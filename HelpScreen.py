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
    pygame.draw.rect(screen, (255, 255, 255), (730,430,60,60))
    pygame.draw.rect(screen, (255, 255, 255), (660,430,60,60))
    pygame.draw.polygon(screen, (0, 0, 255), [(740, 440),(780, 460),
                        (740,480)])
    pygame.draw.polygon(screen, (0, 0, 255), [(670, 460),(710,440),
                        (710,480)])
    font = pygame.font.SysFont("calibri", 30)
    if self.helpScreen == 1:
        text = font.render("Page 1", True, (0, 128, 0))
    elif self.helpScreen == 2:
        text = font.render("Page 2", True, (0, 128, 0))
    elif self.helpScreen == 3:
        text = font.render("Page 3", True, (0, 128, 0))
    elif self.helpScreen == 4:
        text = font.render("Page 4", True, (0, 128, 0))
    else:
        text = font.render("Too far!!", True, (0, 128, 0))
    screen.blit(text, (self.width//2, self.height//2))
    pygame.display.flip()