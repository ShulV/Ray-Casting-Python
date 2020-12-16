from settings import *

# w - wall [8, 12] blocks
text_map = [
    'WWWWWWWWWWWW',
    'W...W...W..W',
    'W..W....W..W',
    'W..W....W..W',
    'W..W....W..W',
    'W..WWWWWW..W',
    'W..........W',
    'W.WWWWWWWWWW'
]

world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i*TILE, j*TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
