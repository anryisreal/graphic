import sys
import pygame
import math

pygame.init()
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
ecliptic = 0


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
            self.ecliptic += self.speed
            self.points.append((self.x, self.y))
        self.ecliptic = 0
        self.x = self.x_gl
        self.y = self.y_gl



sun = Circle(0, 0, 60, (255, 255, 1), 40, 3)
sun.fill_points()
earth = Circle(-50, 0, 20, (30, 87, 222), 300, 4)
earth.fill_points()


def display():
    global ecliptic
    clock = pygame.time.Clock()
    circles = [sun, earth]

    while True:
        clock.tick(60)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for circle in circles:
            circle.draw(screen)
            circle.movement()

        pygame.display.update()


display()
