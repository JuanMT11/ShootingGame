import pygame
import sys
from Player import *
from Enemy import Enemy
from Bala import Bala

pygame.init()

def mostrar_puntuacion(screen, width, puntuacion):
    font = pygame.font.Font(None, 36)
    puntuacion_text = font.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
    puntuacion_rect = puntuacion_text.get_rect(topright=(width - 10, 10))
    screen.blit(puntuacion_text, puntuacion_rect)

def mostrar_menu(screen, width, height, opcion_seleccionada):
    font = pygame.font.Font(None, 36)
    jugar_text = font.render("Jugar", True, (255, 255, 255) if opcion_seleccionada == "Jugar" else (150, 150, 150))
    salir_text = font.render("Salir", True, (255, 255, 255) if opcion_seleccionada == "Salir" else (150, 150, 150))

    jugar_rect = jugar_text.get_rect(center=(width // 2, height // 2 - 20))
    salir_rect = salir_text.get_rect(center=(width // 2, height // 2 + 20))

    screen.blit(jugar_text, jugar_rect)
    screen.blit(salir_text, salir_rect)

def crear_juego():
    jugadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    balas = pygame.sprite.Group()

    jugador = Player(balas)
    jugadores.add(jugador)

    for _ in range(5):
        enemigo = Enemy()
        enemigos.add(enemigo)

    return jugadores, enemigos, balas, jugador

def main():
    width = 800
    height = 551
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Juego Disparos')

    background = pygame.image.load('images/background/bg_2.jpg')

    reloj = pygame.time.Clock()

    jugadores, enemigos, balas, jugador = crear_juego()

    x = 0
    ejecuta = True
    in_menu = True
    opcion_seleccionada = "Jugar"
    enemigos_eliminados = 0
    enemigos_por_nivel = 5
    nivel = 1
    puntuacion = 0  # Nueva variable para la puntuación

    while ejecuta:
        while in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ejecuta = False
                    in_menu = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        opcion_seleccionada = "Jugar"
                    elif event.key == pygame.K_DOWN:
                        opcion_seleccionada = "Salir"
                    elif event.key == pygame.K_RETURN:
                        if opcion_seleccionada == "Jugar":
                            # Reiniciar el juego
                            jugadores, enemigos, balas, jugador = crear_juego()
                            enemigos_eliminados = 0
                            nivel = 1
                            enemigos_por_nivel = 5
                            in_menu = False
                            puntuacion = 0  # Restablecer la puntuación
                        elif opcion_seleccionada == "Salir":
                            ejecuta = False
                            in_menu = False

            mostrar_menu(screen, width, height, opcion_seleccionada)
            pygame.display.flip()
        reloj.tick(18)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecuta = False

        keys = pygame.key.get_pressed()

        for jugador in jugadores:
            jugador.update(keys)
            jugador.jump()

        x_relativa = x % background.get_rect().width
        screen.blit(background, (x_relativa - background.get_rect().width, 0))
        if x_relativa < width:
            screen.blit(background, (x_relativa, 0))

        enemigos.update()
        balas.update()

        for bala in balas.copy():
            if bala.rect.left >= 800:
                balas.remove(bala)

        # Colisión de balas con enemigos
        for bala in balas:
            for enemigo in enemigos:
                if not enemigo.on_skeleton and bala.rect.colliderect(enemigo.rect):
                    enemigo.set_on_skeleton()
                    enemigos_eliminados += 1
                    puntuacion += 1
                    bala.kill()

        # Incrementar nivel
        if enemigos_eliminados >= enemigos_por_nivel:
            nivel += 1
            enemigos_por_nivel *= 2

            for _ in range(enemigos_por_nivel):
                enemigo = Enemy()
                enemigos.add(enemigo)

        # Eliminar enemigos después de la animación del esqueleto
        for enemigo in enemigos.copy():
            if not enemigo.on_skeleton and enemigo.rect.right <= 0:
                enemigo.kill()

        if pygame.sprite.spritecollide(jugador, enemigos, False,pygame.sprite.collide_circle):
            print("Game Over")
            in_menu = True
            opcion_seleccionada = "Jugar"

        jugadores.draw(screen)
        enemigos.draw(screen)
        balas.draw(screen)
        
        mostrar_puntuacion(screen, width, puntuacion)  # Mostrar la puntuación en todo momento

        pygame.display.update()

        x -= 5
        if x <= -background.get_rect().width:
            x = 0

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

