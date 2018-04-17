import pygame

class Camera(object):
    def __init__(self, pos = (0, 0, 0), rot = (0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)
    
    def events(self, event):
        #if event.type == pygame.MOUSEMOTION:
        x,y = event.rel
        x /= 200
        y /= 200
        self.rot[0] += y
        self.rot[1] += x
        
    def update(self, dt, key):
        s = dt*10
        if key[pygame.K_i]: # in future want this to be mouse wheel scroll
            self.pos[2] -= s
        if key[pygame.K_o]:
            if self.pos[2] < -3: # camera cannot go through model
                self.pos[2] += s
        
        #x, y = s*math.sin(self.rot[1]), s*math.cos(self.rot(1))
        
        if key[pygame.K_RIGHT]:
            self.pos[0] -= s
        if key[pygame.K_LEFT]:
            self.pos[0] += s
        if key[pygame.K_DOWN]:
            self.pos[1] -= s
        if key[pygame.K_UP]:
            self.pos[1] += s