import pygame
import json
import random
from typing import Dict
from support import import_csv_layout
from settings import TILESIZE, PLAYER_SIGHT


class Map:
    def __init__(self):
        self.map_size = PLAYER_SIGHT
        self.map_file = "../save/map.json"
        # "x,y": [ [] ] 64*64
        self.map = {}

    def return_map(self) -> Dict:
        return self.map

    def init_map(self, loc: str) -> None:
        with open(self.map_file) as world_map:
            try:
                self.map = json.load(world_map)
            except json.decoder.JSONDecodeError:
                self.map[loc] = [random.choices([22, 44, 66, 88, 110, ], k=self.map_size)] * self.map_size

    def save_map(self) -> None:
        if self.map:
            with open(self.map_file, 'w') as world_map:
                json.dump(self.map, world_map)

    def create_new_chunk(self, loc: str) -> None:
        self.map[loc] = [random.choices([22, 44, 66, 88, 110, ], k=self.map_size)] * self.map_size
