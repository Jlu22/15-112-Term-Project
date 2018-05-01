import pygame
import math
from pygamegame import PygameGame
from Camera import Camera

# Model rotation and view algorithms inspired by:
# https://www.youtube.com/watch?v=g4E9iq0BixA

class Model (object):
    def __init__(self, width, height, keys, verts, edges):
        self.verts = verts
        self.edges = edges
        self.camera = Camera((0, 0, -8))
        self.radians = 0
        self.width = width
        self.height = height
        self.cx = self.width//2 # center of screen
        self.cy = self.height//2
        self.keys = keys
    
    def __eq__(self, object):
        return (isinstance(object, Model) and self.verts == object.verts and
                self.edges == object.edges)
    
    def mouseDrag(self, x, y):
        print("orig",x, y)
        dx, dy = pygame.mouse.get_rel()
        print("rot", dx, dy)
        self.camera.rotate(dx, dy)
    
    def timerFired(self, dt):
        self.camera.update(dt, self.isKeyPressed)
    
    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self.keys.get(key, False)
    
    def redrawAll(self, screen):
        for edge in self.edges:
            points = []
            for x, y, z in (self.verts[edge[0]], self.verts[edge[1]]):
                x -= self.camera.pos[0]
                y -= self.camera.pos[1]
                z -= self.camera.pos[2]
                
                x, z = Camera.rotation((x, z), self.camera.rot[1])
                y, x = Camera.rotation((y, x), self.camera.rot[0])
                
                scale = max(self.width, self.height)//2
                # this scale attempts to maintain good proportions of the part
                
                factor = scale/z # cannot actually draw in 3D, so scale x and y
                x, y = x*factor, y*factor # according to z, give illusion of 3D
                points += [(self.cx+int(x), self.cy+int(y))]
            pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)
