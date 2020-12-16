import pygame
import sys
from math import cos, sin
from settings import *
from player import Player
from map import world_map
from drawing import Drawing
from ray_cating import ray_casting
import wx
import os




class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(WIDTH, HEIGHT))
        self.btn_play = wx.Button(self, label="Играть", size=(100, 100), pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.OnPlay, self.btn_play)
        self.Show(True)
        self.Centre()

    def OnPlay(self, event):
        run_game = True
        pygame.init()
        clock = pygame.time.Clock()  # установка кадров секунду
        player = Player()  # создаем объект - игрок
        distance_to_wall = PLAYER_SPEED * 2
        sc = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))  # мини карта
        drawing = Drawing(sc, sc_map)  # создаем объект - рисовалку
        while run_game:
            for event in pygame.event.get():  # цикл перебора событий
                if event.type == pygame.QUIT:  # выход по нажатию крестика
                    pygame.quit()  # остановка pygame
                    run_game = False
                    return
                    # sys.exit()  # выход из программы
            if not player.movement(distance_to_wall):
                pygame.quit()  # остановка pygame
                run_game = False
                return

            sc.fill(color=BLACK)  # создание окна с черным фоном

            drawing.background()
            distance_to_wall = drawing.world(player_position=player.position, player_direction=player.angle)
            drawing.mini_map(player)

            pygame.display.flip()  # обновление содержимого приложения
            clock.tick(FPS)


app = wx.App(False)
frame = MyFrame(None, 'Игра \"Лабиринт\"')
app.MainLoop()


# основной цикл



