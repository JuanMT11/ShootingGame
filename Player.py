import pygame
from Bala import Bala


class Player(pygame.sprite.Sprite):
    def __init__(self,balas_group):
        super().__init__()
        self.balas_group = balas_group
        self.quieto = pygame.image.load('images/player/quiet/Player_idle2.png')
        self.caminaDerecha = [
            pygame.image.load('images/player/run/run_01.png'),
            pygame.image.load('images/player/run/run_02.png'),
            pygame.image.load('images/player/run/run_03.png'),
            pygame.image.load('images/player/run/run_04.png'),
            pygame.image.load('images/player/run/run_05.png'),
            pygame.image.load('images/player/run/run_06.png'),
            pygame.image.load('images/player/run/run_07.png')
        ]
        self.caminaIzquierda = [
            pygame.image.load('images/player/run/run_01.png'),
            pygame.image.load('images/player/run/run_02.png'),
            pygame.image.load('images/player/run/run_03.png'),
            pygame.image.load('images/player/run/run_04.png'),
            pygame.image.load('images/player/run/run_05.png'),
            pygame.image.load('images/player/run/run_06.png'),
            pygame.image.load('images/player/run/run_07.png')
        ]
        self.salta = [
            pygame.image.load('images/player/jump/jump_01.png'),
            pygame.image.load('images/player/jump/jump_02.png'),
            pygame.image.load('images/player/jump/jump_03.png')
        ]

        self.image = self.quieto  # Inicia con la imagen quieto
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.topleft = (10, 450)
        self.ancho = 126
        self.velocidad = 10
        self.velocidadsalto = -5
        self.cuentaPasos = 0
        self.salto = False
        self.cuentaSalto = 10
        # Disparos
        self.cadencia = 750
        self.ultimo_disparo =  pygame.time.get_ticks()

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > self.velocidad:
            self.rect.x -= self.velocidad
            self.image = self.caminaIzquierda[self.cuentaPasos // 1 % len(self.caminaIzquierda)]
            self.cuentaPasos += 1
        elif keys[pygame.K_RIGHT] and self.rect.right < 800 - self.velocidad:
            self.rect.x += self.velocidad
            self.image = self.caminaDerecha[self.cuentaPasos // 1 % len(self.caminaDerecha)]
            self.cuentaPasos += 1
            
        else:
            self.image = self.quieto
            self.cuentaPasos = 0

        if keys[pygame.K_UP] and self.rect.top > 230:
            self.rect.y -= self.velocidad

        if keys[pygame.K_DOWN] and self.rect.bottom < 551:
            self.rect.y += self.velocidad
        if keys[pygame.K_s]:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia: 
                self.disparo()
                self.ultimo_disparo = ahora
        if not self.salto:
            if keys[pygame.K_SPACE]:
                self.salto = True
                self.image = self.salta[self.cuentaPasos // 1 % len(self.salta)]
                self.cuentaPasos = 0
    def disparo(self):
        nueva_bala = Bala(self.rect.right, self.rect.centery)
        self.balas_group.add(nueva_bala)


    def jump(self):
        if self.salto:
            if self.cuentaSalto >= -10:
                self.rect.y -= (self.cuentaSalto * abs(self.cuentaSalto)) * 0.2
                self.cuentaSalto -= 1
            else:
                self.cuentaSalto = 10
                self.salto = False
    