import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __inti__(self, x, y, radius):
        super.__init__()

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, 2)
    def update(self,dt):
        self.position += self.velocity * dt