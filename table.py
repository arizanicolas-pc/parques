import pygame
import random
import sys
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
NAVY = (0, 51, 102)
LIGHT_BLUE = (173, 216, 230)
HOVER_COLOR = (200, 200, 255)
BACKGROUNG = (30, 30, 60)
GRAY = (128, 128, 128)


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PARQUÉS :D")
clock = pygame.time.Clock()


title_font = pygame.font.SysFont("OCR A Extended", 60, bold=True)
button_font = pygame.font.SysFont("OCR A Extended", 20)
small_font = pygame.font.SysFont("OCR A Extended", 16)


jugadores = {}
turno_actual = 0
orden_jugadores = ["rojo", "verde", "amarillo", "azul"]
casillas = [[] for _ in range(68)]
zonas_llegada = {}
dados = [1, 1]
pares_consecutivos = 0
juego_terminado = False
ganador = None
esperando_input = False
fichas_movibles = []
mensaje_estado = ""


class Button:
     def __init__(self, text, x, y, width=None, height=None, bg=NAVY, text_color=WHITE):
         self.text = text
         self.x = x
         self.y = y
         self.bg = bg
         self.text_color = text_color
         self.padding_x = 20
         self.padding_y = 10

class Button:
     def __init__(self, text, x, y, width=None, height=None, bg=NAVY, text_color=WHITE):
         self.text = text
         self.x = x
         self.y = y
         self.bg = bg
         self.text_color = text_color
         self.padding_x = 20
         self.padding_y = 10
         self.text_surface = button_font.render(self.text, True, text_color)
         text_width, text_height = self.text_surface.get_size()
         self.width = width if width else text_width + 2 * self.padding_x
         self.height = height if height else text_height + 2 * self.padding_y
         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
         def draw(self, screen):
             mouse_pos = pygame.mouse.get_pos()
             is_hovered = self.rect.collidepoint(mouse_pos)
             color = HOVER_COLOR if is_hovered else self.bg
             pygame.draw.rect(screen, color, self.rect, border_radius=10)
             pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=10)
             text_rect = self.text_surface.get_rect(center=self.rect.center)
             screen.blit(self.text_surface, text_rect)
             def is_clicked(self, pos):
                 return self.rect.collidepoint(pos)

class Ficha:
     def __init__(self, jugador, id_ficha):
         self.jugador = jugador
         self.id = id_ficha
         self.estado = "carcel"
         self.posicion = None
         self.posicion_llegada = None
         def __str__(self):
             return str(self.jugador) + "-" + str(Self.id)

             def inicializar_juego():

                 """Inicia el juego con 4 jugadores"""
                 global jugadores, zonas_llegada, turno_actual, pares_consecutivos, juego_terminado
                 global ganador, esperando_input, fichas_movibles, mensaje_estado
                 colores = ["rojo", "verde", "amarillo", "azul"]
                 colores_pygame = [RED, GREEN, YELLOW, BLUE]
                 jugadores = {}
                 for i, color in enumerate(colores):
                     jugadores[color] = {
                     "fichas": [Ficha(color, j) for j in range(4)],
                     "color_pygame": colores_pygame[i]
                     }
                     zonas_llegada[color] = [None for _ in range(8)]
                     turno_actual = 0
                     pares_consecutivos = 0
                     juego_terminado = False
                     ganador = None
                     esperando_input = False
                     fichas_movibles = []
                     mensaje_estado = "HOLAA, SI QUIERES JUGAR, PRESIONA 'LANZAR DADOS':D"
                     for i in range(68):
                         casillas[i] = []
                         def get_casilla_salida(jugador):
                             """Obten la casilla salida segun el jugador"""
                             salidas = {"rojo": 5, "verde": 22, "amarillo": 39, "azul": 56}
                             return salidas.get(jugador, 5)

     def __init__(self, jugador, id_ficha):
         self.jugador = jugador
         self.id = id_ficha
         self.estado = "carcel"
         self.posicion = None
         self.posicion_llegada = None
         def __str__(self):
             return str(self.jugador) + "-" + str(Self.id)

             def inicializar_juego():

                 """Inicia el juego con 4 jugadores"""
                 global jugadores, zonas_llegada, turno_actual, pares_consecutivos, juego_terminado
                 global ganador, esperando_input, fichas_movibles, mensaje_estado
                 colores = ["rojo", "verde", "amarillo", "azul"]
                 colores_pygame = [RED, GREEN, YELLOW, BLUE]
                 jugadores = {}
                 for i, color in enumerate(colores):
                     jugadores[color] = {
                     "fichas": [Ficha(color, j) for j in range(4)],
                     "color_pygame": colores_pygame[i]
                     }
                     zonas_llegada[color] = [None for _ in range(8)]
                     turno_actual = 0
                     pares_consecutivos = 0
                     juego_terminado = False
                     ganador = None
                     esperando_input = False
                     fichas_movibles = []
                     mensaje_estado = "HOLAA, SI QUIERES JUGAR, PRESIONA 'LANZAR DADOS':D"
                     for i in range(68):
                         casillas[i] = []
                         def get_casilla_salida(jugador):
                             """Obten la casilla salida segun el jugador"""
                             salidas = {"rojo": 5, "verde": 22, "amarillo": 39, "azul": 56}
                             return salidas.get(jugador, 5)


class Ficha:
     def __init__(self, jugador, id_ficha):
         self.jugador = jugador
         self.id = id_ficha
         self.estado = "carcel"
         self.posicion = None
         self.posicion_llegada = None
         def __str__(self):
             return str(self.jugador) + "-" + str(Self.id)

             def inicializar_juego():

                 """Inicia el juego con 4 jugadores"""
                 global jugadores, zonas_llegada, turno_actual, pares_consecutivos, juego_terminado
                 global ganador, esperando_input, fichas_movibles, mensaje_estado
                 colores = ["rojo", "verde", "amarillo", "azul"]
                 colores_pygame = [RED, GREEN, YELLOW, BLUE]
                 jugadores = {}
                 for i, color in enumerate(colores):
                     jugadores[color] = {
                     "fichas": [Ficha(color, j) for j in range(4)],
                     "color_pygame": colores_pygame[i]
                     }
                     zonas_llegada[color] = [None for _ in range(8)]
                     turno_actual = 0
                     pares_consecutivos = 0
                     juego_terminado = False
                     ganador = None
                     esperando_input = False
                     fichas_movibles = []
                     mensaje_estado = "HOLAA, SI QUIERES JUGAR, PRESIONA 'LANZAR DADOS':D"
                     for i in range(68):
                         casillas[i] = []
                         def get_casilla_salida(jugador):
                             """Obten la casilla salida segun el jugador"""
                             salidas = {"rojo": 5, "verde": 22, "amarillo": 39, "azul": 56}
                             return salidas.get(jugador, 5)

def get_casillas_seguro():
     """Ve a una casilla segura"""
     return casilla in get_casillas_seguro()

def verificar_bloqueo(casilla):
     """verifica si una casilla está bloqueada"""
     if casilla < 0 or casilla >= 68:
         return False

def verificar_bloqueo(casilla):
     """verifica si una casilla está bloqueada"""
     if casilla < 0 or casilla >= 68:
         return False
         fichas_en_casilla = casillas[casilla]

def verificar_bloqueo(casilla):
     """verifica si una casilla está bloqueada"""
     if casilla < 0 or casilla >= 68:
         return False
         fichas_en_casilla = casillas[casilla]
         if len(fichas_en_casilla) <2:
             return False

def verificar_bloqueo(casilla):
     """verifica si una casilla está bloqueada"""
     if casilla < 0 or casilla >= 68:
         return False
         fichas_en_casilla = casillas[casilla]
         if len(fichas_en_casilla) <2:
             return False
             if len(fichas_en_casilla) >= 2:
                 if fichas_en_casilla[0].jugador == fichas_en_casilla[1].jugador:
                     return True
                     if es_casilla_seguro(casilla):
                         return True
                         return False

def puede_mover_ficha(ficha, pasos):
     """Verifica si una ficha puede moverse"""
     if ficha.estado == "carcel":
         return 5 in dados
         if ficha.estado == "tablero":
             nueva_pos = (ficha.posicion + pasos) % 68
             if verificar_bloqueo(nueva_pos):
                 return False
                 casilla_salida_ = get_casilla_salida(ficha.jugador)
                 pasos_desde_inicio = (ficha.posicion - casilla_salida) % 68
                 if pasos_desde_inicio + pasos >= 68:
                     pasos_en_llegada = (pasos_desde_inicio + pasos) - 68
                     if pasos_en_llegada < 8 and zonas_llegada[ficha.jugador][pasos_en_llegada] is None:
                         return True
                     elif pasos_en_llegada >= 8:
                         return False
                 return True
                 return False

def mover_ficha(ficha, pasos):
     """mueve tu ficha segun los dados"""
     global mensaje_estado
     if ficha.estado == "carcel":
         if 5 in dados:
             casilla_salida = get_casilla_salida(ficha.jugador)
             fichas_en_salida = casillas[casilla_salida][:]
             for f in fichas_en_salida:
                 if f.jugador != ficha.jugador and not es_casilla_seguro(casilla_salida):
                     capturar_ficha(f)
                     mensaje_estado = str(ficha) + "capturó a " + str(f) + "!"
             ficha.estado = "tablero"
             ficha.posicion = casilla_salida
             casillas[casilla_salida].append(ficha)
             mensaje_estado += " " + str(ficha) + "salió de la carcel"
             return True
         elif ficha.estado == "tablero":
             casillas[ficha.posicion].remove(ficha)
             casilla_salida = get_casilla_salida(ficha.jugador)
             pasos_desde_inicio = (ficha.posicion - casilla_salida) % 68
             if pasos_desde_inicio + pasos >= 68:
                 pasos_en_llegada = (pasos_desde_inicio + pasos) - 68
                 if pasos_en_llegada <8 and zonas_llegada[ficha.jugador][pasos_en_llegada] is None:
                     ficha.estado = "llegada"
                     ficha.posicion = None
                     ficha.posicion_llegada = pasos_en_llegada
                     zonas_llegada[ficha.jugador][pasos_en_llegada] = ficha
                     mensaje_estado = str(ficha) + "Estas en zona segura, tranqui :D"
                     return True
                     nueva_pos = (ficha.posicion + pasos) % 68
                     fichas_en_destino = casillas[nueva_pos][:]
                     for f in fichas_en_destino:
                         if f.jugador != ficha.jugador and not es_casilla_seguro(nueva_pos):
                             capturar_ficha(f)
                             mensaje_estado = str(ficha) + " capturó a " + str(f) + "!"
                             ficha.posicion = nueva_pos
                             casillas[nueva_pos].append(ficha)
                             mensaje_estado += " " + str(ficha) + " se movió a casilla " + str(nueva_pos)
                             return False

def capturar_ficha(ficha):
     """Envía una ficha a la carcel"""
     if ficha.estado == "tablero":
         casillas[ficha.posicion].remove(ficha)
     elif ficha.estado == "llegada":
         zonas_llegada[ficha.jugador][ficha.posicion_llegada] = None
         ficha.estado = "carcel"
         ficha.posicion = None
         ficha.posicion_llegada = None
def lanzar_dados():
     """Lanza los dados"""
     return [random.randint(1,6), random.randint(1, 6)]
def obtener_fichas_movibles(jugador):
     """Fichas que pueden moverse"""
     fichas_movibles = []
     suma_dados = sum(dados)

def obtener_fichas_movibles(jugador):
     """Fichas que pueden moverse"""
     fichas_movibles = []
     suma_dados = sum(dados)
     if 5 in dados:
         for ficha in jugadores[jugador]["fichas"]:
             if ficha.estado == "carcel":
                 fichas_movibles.append(ficha)
                 break
     for ficha in jugadores[jugador]["fichas"]:
         if ficha.estado == "tablero" and puede_mover_ficha(ficha, suma_dados):
             fichas_movibles.append(ficha)
             return fichas_movibles

def verificar_ganador():
     """Verifica si hay un ganador"""
     for jugador, data in jugadores.items():
         fichas_en_llegada = sum(1 for f in data["fichas"] if f.estado == "llegada")
         if fichas_en_llegada == 4:
             return jugador
             return None

def avanzar_turno():
     """Avanza al siguiente turno"""
     global turno_actual
     turno_actual = (turno_actual + 1) % 4

def turno_jugador():
     """empieza el turno de un jugador"""
     global pares_consecutivos, esperando_input, fichas_movibles, mensaje_estado
     jugador_actual = orden_jugadores[turno_actual]
     dados[0] = random.randint(1, 6)
     dados[1] = random.randint(1, 6)
     es_par = dados[0] == dados[1]
     if es_par:
         pares_consecutivos += 1
         mensaje_estado = "¡" + jugador_actual.capitalize() + "sacó par! (" + str(dados[0]) + ", " + str(dados[1]) + ")"
     else:
         pares_consecutivos = 0
         mensaje_estado = jugador_actual.capitalize() + " lanzó dados: (" + str(dados[0]) + ", " + str(dados[1]) + ")"
         if pares_consecutivos >= 3:
             mensaje_estado = "Tres pares consecutivos :(, última ficha a la carcel"
         for ficha in reversed(jugadores[jugador_actual]["fichas"]):
             if ficha.estado == "tablero":
                 capturar_ficha(ficha)
                 break
                 pares_consecutivos = 0
                 if not es_par:
                     avanzar_turno()
                     return
                     fichas_movibles = obtener_fichas_movibles(jugador_actual)
                     if not fichas_movibles:
                         mensaje_estado += " - No hay fichas movibles"
                         if not es_par:
                             avanzar_turno()
                             return
                             if len(fichas_movibles) == 1:
                                 mover_ficha(fichas_movibles[0], sum(dados))
                                 verificar_fin_juego()
                                 if not es_par and not juego_terminado:
                                     avanzar_turno()
                             else:
                                 esperando_input = True
                                 mensaje_estado += " - Selecciona una ficha: " + ', '.join([str(f) for f in fichas_movibles])

def verificar_fin_juego():
     """Verifica si el juego terminó"""
     global juego_terminado, ganador
     ganador = verificar_ganador()
     if ganador:
         juego_terminado = True

def seleccionar_ficha(indice):
     """Selecciona una ficha para mover"""
     global esperando_input, mensaje_estado
     if esperando_input and 0 <= indice < len(fichas_movibles):
         ficha_seleccionada = fichas_movibles[indice]
         mover_ficha(ficha_seleccionada, sum(dados))
         esperando_input = False
         verificar_fin_juego()
         es_par = dados[0] == dados[1]
         if not es_par and not juego_terminado:
             avanzar_turno()

def dibujar_dado(screen, valor, x, y, tamaño):
     """dado con el valor especifico"""
     pygame.draw.rect(screen, WHITE, (x, y, tamaño, tamaño))
     pygame.draw.rect(screen, BLACK, (x, y, tamaño, tamaño), e)
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
         pygame.draw.circle(screen, BLACK, posiciones[i], 6)
def dibujar_tablero():
    """Dibuja el tablero visual"""
    # Dibujar círculo del tablero
    pygame.draw.circle(screen, GRAY, (TABLERO_CENTRO_X, TABLERO_CENTRO_Y), TABLERO_RADIO, 3)
    
    
    for i in range(68):
        angulo = (i / 68) * 360
        x = TABLERO_CENTRO_X + int((TABLERO_RADIO - 20) * pygame.math.Vector2(1, 0).rotate(angulo).x)
        y = TABLERO_CENTRO_Y + int((TABLERO_RADIO - 20) * pygame.math.Vector2(1, 0).rotate(angulo).y)
        
        
        color_casilla = LIGHT_BLUE if es_casilla_seguro(i) else WHITE
        pygame.draw.circle(screen, color_casilla, (x, y), 8)
        pygame.draw.circle(screen, BLACK, (x, y), 8, 2)
        
        
        fichas_en_casilla = casillas[i]
        for j, ficha in enumerate(fichas_en_casilla):
            color_ficha = jugadores[ficha.jugador]["color_pygame"]
            offset_x = -6 + (j % 2) * 12
            offset_y = -6 + (j // 2) * 12
            pygame.draw.circle(screen, color_ficha, (x + offset_x, y + offset_y), 4)
    
    
    salidas = {"rojo": 5, "verde": 22, "amarillo": 39, "azul": 56}
    for jugador, casilla in salidas.items():
        angulo = (casilla / 68) * 360
        x = TABLERO_CENTRO_X + int((TABLERO_RADIO - 20) * pygame.math.Vector2(1, 0).rotate(angulo).x)
        y = TABLERO_CENTRO_Y + int((TABLERO_RADIO - 20) * pygame.math.Vector2(1, 0).rotate(angulo).y)
        color = jugadores[jugador]["color_pygame"]
        pygame.draw.circle(screen, color, (x, y), 12, 3)

def dibujar_interfaz():
    """Dibuja la interfaz del juego"""
    screen.fill(BACKGROUND)
    
    
    title = title_font.render("PARQUÉS 4 JUGADORES", True, WHITE)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 30))
    screen.blit(title, title_rect)
    
    
    panel_x = 20
    panel_y = 80
    
  
    if not juego_terminado:
        jugador_actual = orden_jugadores[turno_actual]
        color_actual = jugadores[jugador_actual]["color_pygame"]
        turno_text = f"TURNO: {jugador_actual.upper()}"
        turno_surface = large_font.render(turno_text, True, color_actual)
        screen.blit(turno_surface, (panel_x, panel_y))
    

    dibujar_dado(screen, dados[0], panel_x, panel_y + 40, 50)
    dibujar_dado(screen, dados[1], panel_x + 60, panel_y + 40, 50)
    
    suma_text = f"Suma: {sum(dados)}"
    suma_surface = button_font.render(suma_text, True, WHITE)
    screen.blit(suma_surface, (panel_x + 120, panel_y + 55))
    
   
    info_y = panel_y + 120
    for i, (jugador, data) in enumerate(jugadores.items()):
        color_pygame = data["color_pygame"]
        
   
        nombre_text = f"{jugador.upper()}:"
        nombre_surface = button_font.render(nombre_text, True, color_pygame)
        screen.blit(nombre_surface, (panel_x, info_y))
        
        
        fichas_carcel = sum(1 for f in data["fichas"] if f.estado == "carcel")
        fichas_tablero = sum(1 for f in data["fichas"] if f.estado == "tablero")
        fichas_llegada = sum(1 for f in data["fichas"] if f.estado == "llegada")
        
        estado_text = f"Cárcel: {fichas_carcel} | Tablero: {fichas_tablero} | Llegada: {fichas_llegada}"
        estado_surface = small_font.render(estado_text, True, WHITE)
        screen.blit(estado_surface, (panel_x + 20, info_y + 25))
        
        info_y += 60
    
    
    dibujar_tablero()
    

    if mensaje_estado:
        # Dividir mensaje largo en múltiples líneas
        max_width = 600
        words = mensaje_estado.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if small_font.size(test_line)[0] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        # Mostrar líneas
        mensaje_y = SCREEN_HEIGHT - 100
        for line in lines:
            mensaje_surface = small_font.render(line, True, ORANGE)
            screen.blit(mensaje_surface, (20, mensaje_y))
            mensaje_y += 20

def main():
    """Función principal del juego"""
    global esperando_input, juego_terminado, ganador, mensaje_estado
    
    inicializar_juego()
    
    # Botones
    lanzar_button = Button("Lanzar Dados", 20, SCREEN_HEIGHT - 200, 150, 40)
    reiniciar_button = Button("Nuevo Juego", 200, SCREEN_HEIGHT - 200, 150, 40)
    
    # Botones para seleccionar fichas (solo se muestran cuando hay opciones)
    ficha_buttons = []
    for i in range(4):
        btn = Button(f"Ficha {i+1}", 20 + i * 120, SCREEN_HEIGHT - 150, 100, 30)
        ficha_buttons.append(btn)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                # Botón lanzar dados
                if lanzar_button.is_clicked(pos) and not juego_terminado and not esperando_input:
                    turno_jugador()
                
                # Botón reiniciar
                if reiniciar_button.is_clicked(pos):
                    inicializar_juego()
                
                # Botones de selección de fichas
                if esperando_input:
                    for i, btn in enumerate(ficha_buttons):
                        if i < len(fichas_movibles) and btn.is_clicked(pos):
                            seleccionar_ficha(i)
                
            elif event.type == pygame.KEYDOWN:
                # Teclas numéricas para seleccionar fichas
                if esperando_input:
                    if event.key >= pygame.K_1 and event.key <= pygame.K_4:
                        indice = event.key - pygame.K_1
                        if indice < len(fichas_movibles):
                            seleccionar_ficha(indice)
        
        # Dibujar interfaz
        dibujar_interfaz()
        
        # Dibujar botones
        if not juego_terminado and not esperando_input:
            lanzar_button.draw(screen)
        
        reiniciar_button.draw(screen)
        
        # Dibujar botones de selección de fichas
        if esperando_input:
            instruccion = "Selecciona una ficha (clic o teclas 1-4):"
            instruccion_surface = button_font.render(instruccion, True, WHITE)
            screen.blit(instruccion_surface, (20, SCREEN_HEIGHT - 180))
            
            for i in range(len(fichas_movibles)):
                if i < len(ficha_buttons):
                    # Actualizar texto del botón
                    ficha_buttons[i].text = str(fichas_movibles[i])
                    ficha_buttons[i].text_surface = button_font.render(ficha_buttons[i].text, True, ficha_buttons[i].text_color)
                    ficha_buttons[i].draw(screen)
        
        # Mostrar ganador
        if juego_terminado and ganador:
            ganador_text = f"¡{ganador.upper()} GANA!"
            ganador_surface = title_font.render(ganador_text, True, jugadores[ganador]["color_pygame"])
            ganador_rect = ganador_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            
            # Fondo para el texto del ganador
            pygame.draw.rect(screen, BLACK, ganador_rect.inflate(40, 20))
            pygame.draw.rect(screen, jugadores[ganador]["color_pygame"], ganador_rect.inflate(40, 20), 3)
            screen.blit(ganador_surface, ganador_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()