import pygame

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/gun/Bullet1.png").convert(), (10, 20))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.left = x

    def update(self):
        self.rect.x += 20
        if self.rect.bottom > 551 or self.rect.right > 800:
            self.kill()
