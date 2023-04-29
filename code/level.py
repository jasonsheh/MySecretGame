from settings import *
from tile import Tile
from player import Player
from support import *
# from weapon import Weapon
from tileset import TileSet
from map import Map
from ui import UI


# from npc import NPC


class Level:
    def __init__(self, screen):
        self.screen = screen
        # sprite group setup
        self.visible_sprites = CameraGroup(screen)

        # load map
        self.tileset = TileSet("../data/graphics/tileset/colored-transparent.png").load()
        self.Map = Map()
        self.Map.init_map("0,0")
        self.world_map = self.Map.return_map()

        self.obstacle_sprites = pygame.sprite.Group()

        # user interface
        self.ui = UI(self.screen)
        self.update_map(0, 0)
        self.player = Player(self.screen, (0, 0), (self.visible_sprites,), self.obstacle_sprites)

    def update_map(self, x, y):
        """
        if player at 0,0 sight is 20, load (0,20)(0,-20)(-20,0)(20,0)
        """
        add_map = False
        for _ in [-1 * PLAYER_SIGHT, 0]:
            for __ in [-1 * PLAYER_SIGHT, 0]:
                player_sight_chunk = f"{(x + _ * TILESIZE) // (PLAYER_SIGHT * TILESIZE) * PLAYER_SIGHT}," \
                                     f"{(y + __ * TILESIZE) // (PLAYER_SIGHT * TILESIZE) * PLAYER_SIGHT}"
                if player_sight_chunk not in self.world_map.keys():
                    self.Map.create_new_chunk(player_sight_chunk)
                    add_map = True
        if add_map:
            self.Map.save_map()
            self.world_map = self.Map.return_map()
            self.draw_map()

        # remove chunks that far away from player
        map_chunk_out_screen = []
        for map_chunk in self.world_map.keys():
            loc = [int(_) for _ in map_chunk.split(',')]
            if abs(loc[0] - x) > 800 or abs(loc[1] - y) > 800:
                map_chunk_out_screen.append(map_chunk)
        for _ in map_chunk_out_screen:
            self.world_map.pop(_)
        if map_chunk_out_screen:
            self.draw_map()

    def draw_map(self):
        layouts = {
            'map': self.world_map,
            # 'boundary': import_csv_layout('../map/sample_fantasy_Wall.csv'),
            # 'npc': import_csv_layout('../map/sample_fantasy_NPC.csv'),
        }
        for style, layout in layouts.items():
            for loc, tile_list in layout.items():
                # transfer string location to list
                loc = [int(_) for _ in loc.split(',')]
                for row_index, row in enumerate(tile_list):
                    for col_index, col in enumerate(row):
                        x = (col_index + loc[0]) * TILESIZE
                        y = (row_index + loc[1]) * TILESIZE
                        if style == "map":
                            Tile(self.screen, (x, y), (self.visible_sprites,), 'terrain', self.tileset[col])

    def run(self):
        # update and draw the game
        self.update_map(self.player.rect[0], self.player.rect[1])
        self.visible_sprites.draw_center(self.player)
        self.visible_sprites.update()
        # self.update_npc(self.player)
        self.ui.display(self.player)


class CameraGroup(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def update_npc(self, player):
        npc_sprites = [_ for _ in self.sprites() if _.sprite_type == "npc"]
        for npc in npc_sprites:
            npc.npc_update(player)

    def draw_center(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)
