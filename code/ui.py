import pygame
from settings import *


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # bar
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(self.screen, UI_BG_COLOR, bg_rect)

        # draw bar
        ratio = current / max_amount
        current_width = ratio * bg_rect.width
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.screen, color, current_rect)
        pygame.draw.rect(self.screen, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.screen.get_size()[0] - 20
        y = self.screen.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.screen, UI_BG_COLOR, text_rect.inflate(20,20))
        self.screen.blit(text_surf, text_rect)
        pygame.draw.rect(self.screen, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)

    def selection_box(self, left, top):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.screen, UI_BG_COLOR, bg_rect)
        pygame.draw.rect(self.screen, UI_BORDER_COLOR, bg_rect, 3)

    def display(self, player):
        self.show_bar(player.health, player.stats["health"], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats["energy"], self.energy_bar_rect, ENERGY_COLOR)

        self.show_exp(player.exp)

        self.selection_box(10, 0.8 * self.screen.get_size()[1])
