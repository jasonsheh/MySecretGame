import pygame
from settings import TILESIZE


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.speed = TILESIZE
        self.direction = pygame.math.Vector2()

    def collision(self, direction) -> bool:
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.center == self.rect.center:
                    if self.direction.x > 0:  # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rect.left = sprite.rect.right
                    return True
            return False

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.center == self.rect.center:
                    if self.direction.y < 0:  # moving up
                        self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0:  # moving down
                        self.rect.bottom = sprite.rect.top
                    return True
            return False
