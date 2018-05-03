import pygame
import math

class Camera(object):
    def __init__(self, depth, pos = (0, 0, 0), rot = (0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.depth = depth
    
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
        timePressed = dt/200
        if key(pygame.K_o):
            self.pos[2] -= timePressed
        if key(pygame.K_i):
            if abs(self.depth) < 6:#so camera doesn't go through model
                if self.pos[2] < -3: 
                    self.pos[2] += timePressed
            elif abs(self.depth) < 9:
                if self.pos[2] < -4.5:
                    self.pos[2] += timePressed
            else:
                if self.pos[2] < -6:
                    self.pos[2] += timePressed
        if key(pygame.K_RIGHT):
            self.pos[0] += timePressed
        if key(pygame.K_LEFT):
            self.pos[0] -= timePressed
        if key(pygame.K_DOWN):
            self.pos[1] += timePressed
        if key(pygame.K_UP):
            self.pos[1] -= timePressed
        
        #x, y = s*math.sin(self.rot[1]), s*math.cos(self.rot(1))