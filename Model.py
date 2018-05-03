import pygame
import math
from pygamegame import PygameGame
from Camera import Camera

# Model rotation and view algorithms inspired by:
# https://www.youtube.com/watch?v=g4E9iq0BixA

# almostEqual function from 15-112 website
def almostEqual(d1, d2):
    epsilon = 10**-5
    return (abs(d2 - d1) < epsilon)

class Model (object):
    def __init__(self, width, height, keys, verts, edges):
        self.verts = verts
        self.tmpVerts = []
        for point in self.verts:
            self.tmpVerts.append(list(point))
        print(self.tmpVerts)
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
    
    def __eq__(self, object):
        return (isinstance(object, Model) and self.verts == object.verts and
                self.edges == object.edges)
    
    @staticmethod
    def rotation(pos, rad):
        x, y = pos
        return x*math.cos(rad)-y*math.sin(rad), y*math.cos(rad)+x*math.sin(rad)
    
    def update(self, dt, key):
        timePressed = dt/200
        if key(pygame.K_d):
            self.xyRadians += math.pi / 32
            print("d", self.xyRadians)
        if key(pygame.K_a):
            self.xyRadians -= math.pi / 32
            print("a", self.xyRadians)
        if key(pygame.K_s):
            self.xzRadians += math.pi / 32
            print("s", self.xzRadians)
        if key(pygame.K_w):
            self.xzRadians -= math.pi / 32
            print("w", self.xzRadians)
    
    def timerFired(self, dt):
        self.camera.update(dt, self.isKeyPressed)
        self.update(dt, self.isKeyPressed)
    
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
                
                # x, z = Camera.rotation((x, z), self.camera.rot[1])
                # y, x = Camera.rotation((y, x), self.camera.rot[0])
                
                scale = max(self.width, self.height)//2
                # this scale attempts to maintain good proportions of the part
                
                factor = scale/(z+.0001) # cannot actually draw in 3D, so scale x and y
                x, y = x*factor, y*factor # according to z, give illusion of 3D
                points += [(self.cx+int(x), self.cy+int(y))]
            pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)
