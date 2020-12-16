import pygame
from settings import *
from math import cos, sin


class Player:
    def __init__(self):
        self.x, self.y = START_POSITION
        self.angle = PLAYER_START_ANGLE

    @property
    def position(self):
        return self.x, self.y

    def movement(self, distance_to_wall):
        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
            return False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if distance_to_wall > PLAYER_SPEED*5:
                self.x += PLAYER_SPEED * cos(self.angle)
                self.y += PLAYER_SPEED * sin(self.angle)
            else:
                self.x -= PLAYER_SPEED * cos(self.angle)
                self.y -= PLAYER_SPEED * sin(self.angle)
        if keys[pygame.K_LEFT]:
            self.angle -= ROTATE_ANGLE
        if keys[pygame.K_RIGHT]:
            self.angle += ROTATE_ANGLE
        return True