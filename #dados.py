'''
        I              I
        I I          I I 
        I   III  III   I
        _IIIIIIIIIIIIII_
       I    III  III     I
      I     I I  I I     I
      I     III  III     I
      I   i         i    I
      I    iiiiiiiii     I
        IIIIIIIIIIIIIIII
'''
#datos de pygame
import pygame
import random

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dado prueba #6")
clock = pygame.time.Clock()

def lanzar():
    return random.randint(1, 6)

def dibujar_dado(screen, valor, x, y, tamaño):
    blanco = (255, 255, 255) # con esto se modifica color del fondo del dado
    negro = (0, 0, 0) 
    pygame.draw.rect(screen, blanco, (x, y, tamaño, tamaño))
    pygame.draw.rect(screen, negro, (x, y, tamaño, tamaño), 3) 

    offset = tamaño // 4
    centro = x + tamaño // 2, y + tamaño // 2
    posiciones = [
        (x + offset, y + offset),
        (x + tamaño - offset, y + offset),
        (x + offset, y + tamaño - offset),
        (x + tamaño - offset, y + tamaño - offset),
        centro,
        (x + offset, y + tamaño // 2),
        (x + tamaño - offset, y + tamaño // 2),
    ]

    puntos_por_valor = {
        1: [4],
        2: [0, 3],
        3: [0, 3, 4],
        4: [0, 1, 2, 3],
        5: [0, 1, 2, 3, 4],
        6: [0, 1, 2, 3, 5, 6],
    }

    for i in puntos_por_valor[valor]:
        pygame.draw.circle(screen, negro, posiciones[i], 6)  #hhhhh

# Valores iniciales para los dos dados..... si se mueve esto se va al garete jajajaj
dado_1 = 1
dado_2 = 1
ejecutando = True

# Tamaño y posición.... me dicen que les parece si dejarlos abajo o moverlos arriba
tam_dado = 60
y_dados = 520  
x_dado1 = 50
x_dado2 = 130

while ejecutando:
    screen.fill((255, 0, 255))  # Fondo.... lo dejamos solido o ponemos una imagen de fondo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #no se como hacer botones en la pantalla para poner uno para girar el dado
            dado_1 = lanzar()
            dado_2 = lanzar()

    dibujar_dado(screen, dado_1, x_dado1, y_dados, tam_dado)
    dibujar_dado(screen, dado_2, x_dado2, y_dados, tam_dado)

    pygame.display.flip()
    clock.tick(30) #no le pongan mas de 60....a mi se me fue por error 600 y mi pc dijo adios jajajajaja

pygame.quit()

