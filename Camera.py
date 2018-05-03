# Camera class
# This file contains the camera, which is a viewpoint for each of the models.
# Moving the camera will "move" the model around the screen

import pygame
import math

class Camera(object):
    def __init__(self, depth, pos = (0, 0, 0), rot = (0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.depth = depth
    
    def update(self, dt, key):
        timePressed = dt/200
        if key(pygame.K_o):
            self.pos[2] -= timePressed
        if key(pygame.K_i): #so camera doesn't go through model
            if isinstance(self.depth, float) and abs(self.depth) < 6:
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