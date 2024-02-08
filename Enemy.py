import pygame
import random
from pygame.sprite import AbstractGroup

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imgRandom = random.randrange(6)
        if self.imgRandom == 0:
            self.image = pygame.transform.scale(pygame.image.load("images/enemy/Bat/bat1.png").convert(),(65,65))
            self.caminaIzquierda = [
            pygame.transform.scale(pygame.image.load('images/enemy/Bat/bat1.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Bat/bat2.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Bat/bat3.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Bat/bat4.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Bat/bat5.png').convert(),(65,65))
            ]
            self.cuentaPasos = 0
        if self.imgRandom == 1:
            self.image = pygame.transform.scale(pygame.image.load("images/enemy/fly-eye/fly-eye1.png").convert(),(65,65))
            self.caminaIzquierda = [
            pygame.transform.scale(pygame.image.load('images/enemy/fly-eye/fly-eye1.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/fly-eye/fly-eye2.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/fly-eye/fly-eye3.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/fly-eye/fly-eye4.png').convert(),(65,65))
            ]
            self.cuentaPasos = 0

        if self.imgRandom == 2:
            self.image = pygame.transform.scale(pygame.image.load("images/enemy/Ghost/ghost1.png").convert(),(65,65))
            self.caminaIzquierda = [
            pygame.transform.scale(pygame.image.load('images/enemy/Ghost/ghost1.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Ghost/ghost2.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Ghost/ghost3.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Ghost/ghost4.png').convert(),(65,65))
            ]
            self.cuentaPasos = 0

        if self.imgRandom == 3:
            self.image =  pygame.transform.scale(pygame.image.load("images/enemy/Idle/crab-idle1.png").convert(),(65,65))
            self.caminaIzquierda = [
            pygame.transform.scale(pygame.image.load('images/enemy/Idle/crab-idle1.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Idle/crab-idle2.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Idle/crab-idle3.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/Idle/crab-idle4.png').convert(),(65,65))
            ]
            self.cuentaPasos = 0
        if self.imgRandom == 4:
            self.image =  pygame.transform.scale(pygame.image.load("images/enemy/lizard moves/lizard-move1.png").convert(),(65,65))
            self.caminaIzquierda = [
            pygame.transform.scale(pygame.image.load('images/enemy/lizard moves/lizard-move1.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/lizard moves/lizard-move2.png').convert(),(65,65)),
            pygame.transform.scale(pygame.image.load('images/enemy/lizard moves/lizard-move3.png').convert(),(65,65))
            ]
            self.cuentaPasos = 0
        if self.imgRandom == 5:
            self.image =  pygame.transform.scale(pygame.image.load("images/enemy/Slime/slime1.png").convert(),(65,65))
            self.caminaIzquierda = [
            pygame.transform.scale(pygame.image.load("images/enemy/Slime/slime1.png").convert(),(65,65)),
            pygame.transform.scale(pygame.image.load("images/enemy/Slime/slime2.png").convert(),(65,65)),
            pygame.transform.scale(pygame.image.load("images/enemy/Slime/slime3.png").convert(),(65,65)),
            pygame.transform.scale(pygame.image.load("images/enemy/Slime/slime4.png").convert(),(65,65)),
            pygame.transform.scale(pygame.image.load("images/enemy/Slime/slime5.png").convert(),(65,65))
            ]
            self.cuentaPasos = 0

        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(700, 800 - self.rect.width)
        self.rect.y =  random.randrange(250,500)
        self.velocidad_x = random.randrange(1,5)
        
        self.skeleton_image = pygame.image.load("images/dead/skeleton-idle1.png").convert()
        self.skeleton_image = pygame.transform.scale(self.skeleton_image, (65, 65))
        self.skeleton_image.set_colorkey((0, 0, 0))
        self.on_skeleton = False
        self.skeleton_steps = 0
        self.max_skeleton_steps = 5 * 18  # Ajusta este valor según sea necesario (5 segundos a 18 FPS)

        
    def update(self):
        if not self.on_skeleton:
            self.rect.x -= self.velocidad_x
            if self.rect.x < 0:
                self.rect.x = random.randrange(700, 800 - self.rect.width)
                self.rect.y = random.randrange(250,500)
                self.velocidad_x = random.randrange(1,5)
            self.image = self.caminaIzquierda[self.cuentaPasos // 1 % len(self.caminaIzquierda)]
            self.image.set_colorkey((0,0,0))
            self.radius = 25
            self.cuentaPasos += 1
        else:
            self.image = self.skeleton_image
            self.skeleton_steps += 1
            if self.skeleton_steps >= self.max_skeleton_steps:
                self.on_skeleton = False
                self.skeleton_steps = 0
                self.kill()  # Elimina al enemigo del grupo
    def set_on_skeleton(self):
        self.on_skeleton = True

