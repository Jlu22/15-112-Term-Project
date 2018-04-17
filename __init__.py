import pygame
import math
from pygamegame import PygameGame
from Camera import Camera

class Model (PygameGame):
    def init(self):
        self.bgColor = (255, 255, 255)
        self.verts = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1),(1, 1, 1), (-1, 1, 1)] # basic points of a cube... just for testing
        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
        self.camera = Camera((0, 0, -10))
        self.radians = 0
        self.cx = self.width//2 # center of screen
        self.cy = self.height//2
    
    def keyPressed(self, code, modifier):
        pass
    
    def timerFired(self, dt):
        self.camera.update(dt, self.isKeyPressed)
    
    def redrawAll(self, screen):
        for edge in self.edges:
            points = []
            for x, y, z in (self.verts[edge[0]], self.verts[edge[1]]):
                x -= self.camera.pos[0]
                y -= self.camera.pos[1]
                z -= self.camera.pos[2]
                
                # x, z = rotate((x, z), radian)
                # y, z = rotate((y, z), radian)
                
                scale = max(self.width, self.height)//2
                # this scale attempts to maintain good proportions of the part
                
                factor = scale/z # cannot actually draw in 3D, so scale x and y
                x, y = x*factor, y*factor # according to z, give illusion of 3D
                points += [(self.cx+int(x), self.cy+int(y))]
            pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)


Model(800, 500).run()