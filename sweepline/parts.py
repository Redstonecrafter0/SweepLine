import pygame
import random as rand

class LineManager:
    instance = None

    def __init__(self, line):
        self.line = line

    def update(self, surface):
        self.line.tick(surface)

class Point:
    screenRes = (0, 0)

    def __init__(self, x, y, speedMin, speedMax):
        self.x = x
        self.y = y
        self.vx = rand.randint(speedMin, speedMax)
        self.vy = rand.randint(speedMin, speedMax)

    def tick(self):
        if self.x <= 0 or self.x >= Point.screenRes[0]:
            self.vx *= -1
        if self.y <= 0 or self.y >= Point.screenRes[1]:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy

class Line:
    lifetime = 0

    def __init__(self, p1, p2, color, rise):
        self.p1 = p1
        self.p2 = p2
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.rr = rise[0]
        self.gr = rise[0]
        self.br = rise[0]

    def tick(self, surface):
        if self.r < 255 and self.rr:
            self.r += 1
        elif self.r > 0 and not self.rr:
            self.r -= 1
        if (self.r == 0) or (self.r == 255):
            self.rr = not self.rr
        if self.g < 255 and self.gr:
            self.g += 1
        elif self.g > 0 and not self.gr:
            self.g -= 1
        if (self.g == 0) or (self.g == 255):
            self.gr = not self.gr
        if self.b < 255 and self.br:
            self.b += 1
        elif self.b > 0 and not self.br:
            self.b -= 1
        if (self.b == 0) or (self.b == 255):
            self.br = not self.br
        l = LineCopy(self.p1, self.p2, (self.r, self.g, self.b), Line.lifetime)
        l.draw(surface)
        return l

class LineCopy:
    def __init__(self, p1, p2, color, lifetime):
        self.p1 = p1
        self.p2 = p2
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.a = 255

    def draw(self, surface):
        pygame.draw.line(surface, (self.r, self.g, self.b, self.a), (self.p1.x, self.p1.y), (self.p2.x, self.p2.y))
