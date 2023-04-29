import pygame
from settings import *


class FPS:
    def __init__(self, font):
        self.clock = pygame.time.Clock()
        self.font = font
        self.text = self.font.render(str(int(self.clock.get_fps())), True, TEXT_COLOR)

    def render(self, display):
        self.text = self.font.render(str(int(self.clock.get_fps())), True, TEXT_COLOR)
        display.blit(self.text, (20, 20))
