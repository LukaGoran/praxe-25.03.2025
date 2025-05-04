import pygame
import sys
from main import Main  # Ujisti se, ze mas tridu Main ve svem main.py
from colors import Colors

class TetrisMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 622))

        # Načtení pozadí
        self.background = pygame.image.load("image/MenuC.png")
        self.background = pygame.transform.scale(self.background, (500, 622))

        # Barvy a fonty
        self.title_font = pygame.font.SysFont('arial', 50, bold=True)
        self.menu_font = pygame.font.SysFont('arial', 35)

        self.options = ["START GAME", "CONTROLS", "QUIT"]
        self.selected = 0

    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.set_caption("Tetris Menu")

        # Titulek
        title = self.title_font.render("TETRIS", True, Colors.modra)
        self.screen.blit(title, (self.screen.get_width() // 2 - title.get_width() // 2, 80))

        # Možnosti menu
        for i, option in enumerate(self.options):
            color = Colors.bila if i != self.selected else Colors.cervena
            text = self.menu_font.render(option, True, color)
            x = self.screen.get_width() // 2 - text.get_width() // 2
            y = 200 + i * 70
            self.screen.blit(text, (x, y))

            if i == self.selected:
                arrow_x = x - 30
                arrow = self.menu_font.render(">", True, Colors.cervena)
                self.screen.blit(arrow, (arrow_x, y))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected == 0:  # START GAME
                            game = Main(self.screen)
                            game.run()
                        elif self.selected == 1:  # CONTROLS
                            self.show_controls()
                        elif self.selected == 2:  # QUIT
                            running = False

            self.draw_menu()
            pygame.display.flip()

    def show_controls(self):
        running = True
        font = pygame.font.SysFont('arial', 25)
        back_text = font.render("Press ESC to go back", True, Colors.bila)
        lines = [
            " ←-→ - Move",
            " ↑ - Rotate",
            " ↓  - Soft Drop",
        ]
        while running:
            self.screen.blit(self.background, (0, 0))
            for i, line in enumerate(lines):
                text = font.render(line, True, Colors.bila)
                self.screen.blit(back_text, (110, 380))
                self.screen.blit(text, (100, 200 + i * 40))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

if __name__ == "__main__":
    menu = TetrisMenu()
    menu.run()
    pygame.quit()
    sys.exit()