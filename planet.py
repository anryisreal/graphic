import math
import pygame
width, height = 980, 980


class Circle:

    def __init__(self, x, y, r, color, orbit, speed):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.x_gl = x
        self.y_gl = y
        self.orbit = orbit
        self.speed = speed
        self.ecliptic = 0
        self.points = []

    def draw(self, screen):
        x = self.x + width / 2
        y = self.y + height / 2
        pygame.draw.circle(screen, self.color, (x, y), self.r)
        pygame.draw.lines(screen, self.color, False, self.points, 2)

    def movement(self):
        if self.ecliptic <= 360:
            angle = self.ecliptic * (math.pi / 180)
            self.x = self.orbit * math.cos(angle) + self.x_gl
            self.y = self.orbit * math.sin(angle) + self.y_gl
            self.ecliptic += self.speed
        else:
            self.ecliptic = 0

    def fill_points(self):
        while self.ecliptic <= 360:
            angle = self.ecliptic * (math.pi / 180)
            self.x = self.orbit * math.cos(angle) + self.x_gl + width / 2
            self.y = self.orbit * math.sin(angle) + self.y_gl + height / 2
            self.ecliptic += 0.1
            self.points.append((self.x, self.y))
        self.ecliptic = 0
        self.x = self.x_gl
        self.y = self.y_gl
