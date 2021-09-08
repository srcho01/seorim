# -*- coding: utf-8 -*-

import pygame
import random as rnd

class Bullet:
    def __init__(self, radius, color):
        self.pos = [0, rnd.random()*800]
        self.to = [rnd.random()-0.5, rnd.random()-0.5]
        self.radius = radius
        self.color = color
    def update_and_draw(self, dt, screen): 
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0]) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1]) % height
        pygame.draw.circle(screen, self.color, self.pos, self.radius)