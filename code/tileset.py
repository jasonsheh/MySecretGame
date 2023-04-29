import pygame
from typing import List


class TileSet:
    def __init__(self, file: str, size=(16, 16), margin=1, spacing=1):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect()
        self.tiles = []

    def load(self) -> List:

        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)
        return self.tiles

    def __str__(self) -> str:
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size} quantity: {len(self.tiles)}'


if __name__ == '__main__':
    t = TileSet("../data/graphics/tileset/colored-transparent.png")
    t.load()
    print(t)
