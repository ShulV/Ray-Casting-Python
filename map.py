from settings import *

text_map_name = 'Text_maps/map1.txt'


class Map:
    def __init__(self):
        self.world_map = set()
        self.mini_map = set()
        # w - wall [8, 12] blocks
        # value for example (not used)
        self.text_map = [
            'WWWWWWWWWWWW',
            'W...W...W..W',
            'W..W....W..W',
            'W..W....W..W',
            'W..W....W..W',
            'W..WWWWWW..W',
            'W..........W',
            'W.WWWWWWWWWW'
        ]

    def load_text_map(self, filename):
        with open(filename, 'r', encoding='utf8') as file:
            for line in enumerate(file):
                self.text_map[line[0]] = line[1][0:12]
        for x in self.text_map:
            print(x)

    def fill_points_of_maps(self):
        self.world_map.clear()
        self.mini_map.clear()
        for j, row in enumerate(self.text_map):
            for i, char in enumerate(row):
                if char == 'W':
                    self.world_map.add((i * TILE, j * TILE))
                    self.mini_map.add((i * MAP_TILE, j * MAP_TILE))


map_obj = Map()
map_obj.load_text_map(text_map_name)
map_obj.fill_points_of_maps()
