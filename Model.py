# Model class
# This file contains the calculations for a "3D" like image from a set of given
# verticies and edges from the model mode. Each model has a camera.
# This file also controls rotation of the model.

import pygame
import math
from pygamegame import PygameGame
from Camera import Camera

# Model rotation and view algorithms inspired by:
# https://www.youtube.com/watch?v=g4E9iq0BixA

class Model (object):
    def __init__(self, width, height, keys, verts, edges):
        self.verts = verts
        self.tmpVerts = []
        for point in self.verts:
            self.tmpVerts.append(list(point))
        self.depth = self.verts[0][2] * 2
        self.edges = edges
        self.camera = Camera(self.depth, (0, 0, -8))
        self.xyRadians = 0
        self.xzRadians = 0
        self.width = width
        self.height = height
        self.cx = self.width//2 # center of screen
        self.cy = self.height//2
        self.keys = keys
    
    @staticmethod
    def rotation(pos, rad):
        x, y = pos
        return x*math.cos(rad)-y*math.sin(rad), y*math.cos(rad)+x*math.sin(rad)
    
    def update(self, key):
        if key(pygame.K_d):
            self.xzRadians -= math.pi / 128 # translational motion
        if key(pygame.K_a):
            self.xzRadians += math.pi / 128
        if key(pygame.K_s):
            self.xyRadians -= math.pi / 128 # rotational motion
        if key(pygame.K_w):
            self.xyRadians += math.pi / 128
    
    def timerFired(self, dt):
        self.camera.update(dt, self.isKeyPressed)
    
    def rotate(self):
        self.update(self.isKeyPressed)
    
    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self.keys.get(key, False)
    
    def redrawAll(self, screen):
        for edge in self.edges:
            points = []
            for x, y, z in (self.tmpVerts[edge[0]], self.tmpVerts[edge[1]]):
                x -= self.camera.pos[0]
                y -= self.camera.pos[1]
                z -= self.camera.pos[2]
                
                x, y = Model.rotation((x,y), self.xyRadians)
                x, z = Model.rotation((x,z), self.xzRadians)
                
                scale = max(self.width, self.height)//2
                # this scale attempts to maintain good proportions of the part
                
                factor = scale/(z+.0001) # cannot actually draw in 3D, so scale x and y
                x, y = x*factor, y*factor # according to z, give illusion of 3D
                points += [(self.cx+int(x), self.cy+int(y))]
            pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)
