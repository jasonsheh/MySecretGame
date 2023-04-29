import pygame
from entity import Entity


class NPC(Entity):
    def __init__(self, screen, name, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.sprite_type = "npc"
        self.screen = screen
        self.import_graphics(name)
        self.image = pygame.image.load("../data/graphics/test/ghost.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.screen.blit(self.image, pos)
        self.obstacle_sprites = obstacle_sprites

        self.step = True

        # stats
        self.NPC_name = name
        self.health = 100
        self.exp = 10
        self.attack_damage = 10
        self.status = "idle"

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)

        distance = (player_vec - enemy_vec).magnitude()
        direction = (player_vec - enemy_vec)

        return distance, direction

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]
        if distance <= 16:
            self.status = "attack"
        elif distance < 100:
            self.status = "search"
        else:
            self.status = "idle"

    def actions(self, player):
        if self.status == 'attack':
            pass
            # self.attack_time = pygame.time.get_ticks()
            # self.damage_player(self.attack_damage, self.attack_type)
            # self.attack_sound.play()
        elif self.status == 'search':
            self.direction = self.get_player_distance_direction(player)[1]
            moved = False
            if self.direction.x > 0 and not moved:
                self.rect.x += self.speed
                if self.collision("horizontal"):
                    self.rect.x -= self.speed
                else:
                    moved = True

            if self.direction.x < 0 and not moved:
                self.rect.x -= self.speed
                if self.collision("horizontal"):
                    self.rect.x += self.speed
                else:
                    moved = True

            if self.direction.y > 0 and not moved:
                self.rect.y += self.speed
                if self.collision("vertical"):
                    self.rect.y -= self.speed
                else:
                    moved = True

            if self.direction.y < 0 and not moved:
                self.rect.y -= self.speed
                if self.collision("vertical"):
                    self.rect.y += self.speed
                else:
                    moved = True

        else:
            self.direction = pygame.math.Vector2()

    def import_graphics(self, name):
        pass

    def npc_update(self, player):
        self.get_status(player)
        if player.step and self.step:
            self.actions(player)
            self.step = False

        if not player.step:
            self.step = True
