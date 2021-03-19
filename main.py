import os
import pygame
import ctypes
import random as rand
from sweepline import parts

# os.environ['SDL_VIDEO_CENTERED'] = '1'

fullscreen = False

if fullscreen:
    screenRes = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
else:
    screenRes = (800, 450)

parts.Point.screenRes = screenRes
parts.Line.screenRes = screenRes
parts.Line.lifetime = 255

pygame.init()

if fullscreen:
    screen = pygame.display.set_mode(screenRes, pygame.NOFRAME)
else:
    screen = pygame.display.set_mode(screenRes)
pygame.display.set_caption('Sweep Line')
clock = pygame.time.Clock()
screen.fill((0, 0, 0))

p1 = parts.Point(rand.randint(1, screenRes[0]), rand.randint(1, screenRes[1]), 8, 10)
p2 = parts.Point(rand.randint(1, screenRes[0]), rand.randint(1, screenRes[1]), -10, -8)
line = parts.Line(p1, p2, (255, 130, 20), (True, False, True))
parts.LineManager.instance = parts.LineManager(line)
surface = pygame.Surface(screenRes, pygame.SRCALPHA).convert_alpha()

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[pygame.K_LALT] and pygame.key.get_pressed()[pygame.K_F4]):
            quit(0)
    p1.tick()
    p2.tick()
    pygame.draw.rect(surface, (0, 0, 0, 1), pygame.Rect((0, 0), screenRes))
    parts.LineManager.instance.update(surface)
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    clock.tick(20)
