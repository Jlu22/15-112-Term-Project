import pygame
import math

class Camera(object):
    def __init__(self, pos = (0, 0, 0), rot = (0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)
    
    def rotate(self, x, y):
        x /= 200
        y /= 200
        self.rot[0] += y
        self.rot[1] += x
        print(self.rot[0], self.rot[1])
    
    @staticmethod
    def rotation(pos, rad):
        x, y = pos
        return x*math.cos(rad)-y*math.sin(rad), y*math.cos(rad)+x*math.sin(rad)
        
    def update(self, dt, key):
        timePressed = dt/100
        if key(pygame.K_o):
            self.pos[2] -= timePressed
        if key(pygame.K_i):
            if self.pos[2] < -3: # so camera doesn't go through model
                self.pos[2] += timePressed
        if key(pygame.K_RIGHT):
            self.pos[0] += timePressed
        if key(pygame.K_LEFT):
            self.pos[0] -= timePressed
        if key(pygame.K_DOWN):
            self.pos[1] += timePressed
        if key(pygame.K_UP):
            self.pos[1] -= timePressed
        
        if key(pygame.K_SPACE):
            self.pos = [0, 0, -5]
        
        #x, y = s*math.sin(self.rot[1]), s*math.cos(self.rot(1))