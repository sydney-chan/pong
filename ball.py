import pygame
from random import randint
teal = (10,118,135)
white = (255,255,255)

class Ball(pygame.sprite.Sprite):
    def randomize():
        self.velocity = [randint(4,8), randint(-8,8)]

    def __init__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w,h])
        self.image.fill(teal)
        self.image.set_colorkey(teal)

        pygame.draw.rect(self.image, color, [0,0,w,h])

        self.velocity = [0,0]
        while self.velocity[1] == 0:
            self.velocity = [randint(4,8), randint(-8,8)]

        self.rect = self.image.get_rect()


    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]



    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
