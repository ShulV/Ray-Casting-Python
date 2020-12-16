import pygame
from settings import *
from ray_cating import ray_casting
from map import mini_map


class Drawing:
    """Рисующий класс"""
    def __init__(self, sc, sc_map):
        self.sc = sc  # экран
        self.sc_map = sc_map  # мини карта
        self.font = pygame.font.SysFont('Arial', 16, bold=True)  # шрифт

    def background(self):
        """Рисование неба и пола"""
        pygame.draw.rect(self.sc, color=GROUND_COLOR, rect=(0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, color=SKY_COLOR, rect=(0, 0, WIDTH, HALF_HEIGHT))

    def world(self, player_position, player_direction):
        """Рисование стен (мира)"""
        return ray_casting(self.sc, player_pos=player_position, player_angle=player_direction)

    def fps(self, clock):
        """Показ фпс на экране"""
        display_fps = str(int(clock.get_fps()))
        render = self.font.render("FPS " + display_fps, True, BLACK)
        self.sc.blit(render, FPS_POSITION)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, PURPLE, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, GREEN, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, WHITE, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)
