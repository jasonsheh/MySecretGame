import pygame
from settings import TILESIZE
from entity import Entity
from support import import_folder


class Player(Entity):
    def __init__(self, screen, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../data/graphics/test/People.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.screen = screen
        self.screen.blit(self.image, pos)

        self.sprite_type = "player"

        # graphics setup
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # movement
        self.step = False
        self.round_cooldown = 200
        self.round_time = None

        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

        # stats
        self.stats = {
            "health": 100,
            "energy": 60,
            'attack': 10,
            "magic": 4,
            "speed": 6,
        }
        self.health = self.stats["health"]
        self.energy = self.stats["energy"]
        self.exp = 123

    def input(self):
        if not self.step:
            keys = pygame.key.get_pressed()

            # movement input
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
                self.step = True
                self.round_time = pygame.time.get_ticks()
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
                self.step = True
                self.round_time = pygame.time.get_ticks()
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
                self.step = True
                self.round_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
                self.step = True
                self.round_time = pygame.time.get_ticks()
            else:
                self.direction.x = 0

            self.rect.x += self.direction.x * self.speed
            self.collision("horizontal")
            self.rect.y += self.direction.y * self.speed
            self.collision("vertical")

            # attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()

            # magic input
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

        if self.step:
            if current_time - self.round_time >= self.round_cooldown:
                self.step = False

    def update(self) -> None:
        self.input()
        self.cooldown()
