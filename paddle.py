import pygame

teal = (10,118,135)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w,h])
        self.image.fill(teal)
        self.image.set_colorkey(teal)

        pygame.draw.rect(self.image, color, [0,0,w,h])

        self.rect = self.image.get_rect()



    def moveup(self, pixels):
        self.rect.y -= pixels
        if self.rect.y<0:
            self.rect.y = 0


    def movedown(self, pixels):
        self.rect.y += pixels
        if self.rect.y>400:
            self.rect.y = 400
