import pygame
import sys
from game import Game
from colors import Colors

class Main:
    def __init__(self, screen):
        self.screen = screen  # okno z menu
        self.clock = pygame.time.Clock()
        self.game = Game()

        # Textové fonty a nápisy
        self.title_font = pygame.font.Font(None, 40)
        self.score_surface = self.title_font.render("Score", True, Colors.bila)
        self.next_surface = self.title_font.render("Next", True, Colors.bila)
        self.game_over_surface = self.title_font.render("GAME OVER", True, Colors.bila)
        self.high_score_surface = self.title_font.render("High Score", True, Colors.bila)

        # Obdélníky pro body a další blok
        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.high_score_rect = pygame.Rect(320, 500, 170, 65)
        self.next_rect = pygame.Rect(320, 215, 170, 180)

        # Událost pro pád bloku
        self.GAME_UPDATE = pygame.USEREVENT
        self.initial_speed = 500
        pygame.time.set_timer(self.GAME_UPDATE, self.initial_speed)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                # Klávesy
                if event.type == pygame.KEYDOWN:
                    if self.game.game_over:
                        self.game.reset()
                        self.game.game_over = False
                        pygame.time.set_timer(self.GAME_UPDATE, self.initial_speed)
                    if not self.game.game_over:
                        if event.key == pygame.K_LEFT:
                            self.game.move_left()
                        if event.key == pygame.K_RIGHT:
                            self.game.move_right()
                        if event.key == pygame.K_DOWN:
                            self.game.move_down()
                            self.game.update_score(0, 1)
                        if event.key == pygame.K_UP:
                            self.game.rotate()

                # Automatický pád
                if event.type == self.GAME_UPDATE and not self.game.game_over:
                    self.game.move_down()

                    if self.game.score > 1500:
                        pygame.time.set_timer(self.GAME_UPDATE, 200)
                    if self.game.score > 3000:
                        pygame.time.set_timer(self.GAME_UPDATE, 100)

            self.draw()
            pygame.display.update()
            self.clock.tick(60)

            # Konec hry
            if self.game.game_over:
                self.show_game_over()
                return  # návrat do menu

    def draw(self):
        self.screen.fill(Colors.lososova)

        self.screen.blit(self.score_surface, (365, 20))
        self.screen.blit(self.next_surface, (375, 180))
        self.screen.blit(self.high_score_surface, (330, 470))

        # Hodnoty skóre
        score_value = self.title_font.render(str(self.game.score), True, Colors.bila)
        high_score_value = self.title_font.render(str(self.game.high_score), True, Colors.bila)

        pygame.draw.rect(self.screen, Colors.svetla_modra, self.score_rect, 0, 30)
        pygame.draw.rect(self.screen, Colors.svetla_modra, self.high_score_rect, 0, 30)
        pygame.draw.rect(self.screen, Colors.svetla_modra, self.next_rect, 0, 100)

        self.screen.blit(score_value, score_value.get_rect(center=self.score_rect.center))
        self.screen.blit(high_score_value, high_score_value.get_rect(center=self.high_score_rect.center))

        self.game.draw(self.screen)

    def show_game_over(self):
        self.screen.fill(Colors.cerna)
        pygame.draw.rect(self.screen, Colors.fialova, [150, 90, 200, 100], 10, 10)
        pygame.draw.rect(self.screen, Colors.cervena, [150, 243, 200, 100], 10, 10)
        pygame.draw.rect(self.screen, Colors.modra, [150, 400, 200, 100], 10, 10)

        self.screen.blit(self.game_over_surface, (165, 280))
        self.screen.blit(self.high_score_surface, (175, 110))

        high_score_value = self.title_font.render(str(self.game.high_score), True, Colors.bila)
        self.screen.blit(high_score_value, (215, 150))

        self.screen.blit(self.score_surface, (210, 420))
        score_value = self.title_font.render(str(self.game.score), True, Colors.bila)
        self.screen.blit(score_value, score_value.get_rect(center=(250, 470)))

        pygame.display.flip()
        pygame.time.wait(3000)  # pauza na zobrazení
