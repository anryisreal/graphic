import sys
import pygame
from planet import Circle

pygame.init()
WIDTH, HEIGHT = 980, 980
screen = pygame.display.set_mode((WIDTH, HEIGHT))
ecliptic = 0


sun = Circle(0, 0, 60, (255, 255, 1), 40, 3)
earth = Circle(0, 0, 20, (30, 87, 222), 300, 4)
mars = Circle(0, 0, 18, (203, 27, 27), 420, 3)
circles = [sun, earth, mars]
for circle in circles:
    circle.fill_points()


def display():
    global ecliptic
    clock = pygame.time.Clock()

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
