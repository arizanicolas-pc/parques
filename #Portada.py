import pygame
pygame.init()

# portada
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("PARQUÉS :D")
clock = pygame.time.Clock()

# color
WHITE = (255, 255, 255)
NAVY = (0, 51, 102)
LIGHT_BLUE = (173, 216, 230)
HOVER_COLOR = (200, 200, 255)
BACKGROUND = (30, 30, 60)

# tipo de letras
title_font = pygame.font.SysFont("OCR A Extended", 60, bold=True)
button_font = pygame.font.SysFont("OCR A Extended", 30)

class Button:
    def __init__(self, text, num, comp, pos, bg=NAVY, padding_x=40, padding_y=15):
        self.text = text
        self.num = num
        self.comp = comp
        self.x, self.y = pos
        self.bg = bg
        self.padding_x = padding_x
        self.padding_y = padding_y

       
        self.text_surface = button_font.render(self.text, True, WHITE)
        text_width, text_height = self.text_surface.get_size()

        
        self.width = text_width + 2 * padding_x
        self.height = text_height + 2 * padding_y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def show(self):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        color = HOVER_COLOR if is_hovered else self.bg

        pygame.draw.rect(screen, color, self.rect, border_radius=15)

        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    global n, withComputer
                    n = self.num
                    withComputer = self.comp
                    print(n, ",", withComputer)
                    pygame.quit()
                    mainGame()


def draw_title():
    # diseño de recuadro
    shadow = title_font.render(":D PARQUÉS :D", True, (0, 0, 0))
    shadow_rect = shadow.get_rect(center=(502, 102))
    screen.blit(shadow, shadow_rect)

    # titulo
    title = title_font.render(":D PARQUÉS :D", True, (255, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    screen.blit(title, title_rect)

def mainloop():
    while True:
        screen.fill(BACKGROUND)
        draw_title()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            for button in buttons:
                button.click(event)

        for button in buttons:
            button.show()

        clock.tick(60)
        pygame.display.update()

# botones
buttons = [
    Button("Tu vs el computador :D", 2, True, (270, 180)),
    Button("2 jugadores :D", 2, False, (350, 260)),
    Button("3 jugadores :D", 3, False, (350, 340)),
    Button("4 jugadores :D", 4, False, (350, 420)),
]

mainloop()

