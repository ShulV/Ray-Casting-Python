import pygame
import sys
from math import cos, sin
from settings import *
from player import Player
from map import map_obj
from drawing import Drawing
from ray_cating import ray_casting
import wx
import os


class Frame(wx.Frame):
    """ We simply derive a new class of Frame. """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(WIDTH, HEIGHT))
        self.Bind(wx.EVT_CLOSE, self.on_close, self)

        # Setting up the menu.
        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&О программе", " Information about this program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&Справка")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        # Events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

    def OnAbout(self, e):
        # Create a message dialog box
        about_text = "Программа представляет собой игру 'Лабиринт', состоящую из 5 уровней.\n" \
                     "Управление осуществляется с помощью клавиш W (движение вперёд) и стрелок влево и вправо (для " \
                     "поворота).\n" \
                     "Уровень считается пройденным, если игрок вышел за пределы лабиринта\n" \
                     "В данной версии игры не предусмотрено сохранение данных, если вы выйдете, прогресс обнулится."
        dlg = wx.MessageDialog(self, caption='О программе', message=about_text, style=wx.OK,)
        dlg.ShowModal()  # Shows it
        dlg.Destroy()  # finally destroy it when finished.

    def on_close(self, event):
        self.Show(False)
        sys.exit()


class LevelsPanel(wx.Panel):
    def __init__(self, parent, quantity_btn):
        wx.Panel.__init__(self, parent)
        # A button
        self.btn_back = wx.Button(self, label='Назад', pos=(WIDTH - 200, HEIGHT - 120), size=(150, 50))
        self.Bind(wx.EVT_BUTTON, self.on_back, self.btn_back)
        self.btn_levels = list()
        for btn_num in range(0, quantity_btn):
            pos = (70 + btn_num * 140, 70)
            btn = wx.Button(self, id=btn_num, label=str(btn_num + 1), pos=pos, size=(70, 70))
            self.Bind(wx.EVT_BUTTON, self.on_play, btn, id=btn_num + 1)
            self.btn_levels.append(btn)

    def on_back(self, event):
        global main_frame, levels_frame
        levels_frame.Show(False)
        main_frame.Show(True)

    def on_play(self, event):
        btn_name = event.GetEventObject().GetLabel()
        filename = f'Text_maps/map{btn_name}.txt'
        map_obj.load_text_map(filename)
        map_obj.fill_points_of_maps()
        global levels_frame
        levels_frame.Show(False)
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
                    main_frame.Show(True)
                    return
                    # sys.exit()  # выход из программы
            if not player.movement(distance_to_wall):
                pygame.quit()  # остановка pygame
                run_game = False
                main_frame.Show(True)
                return

            sc.fill(color=BLACK)  # создание окна с черным фоном

            drawing.background()
            distance_to_wall = drawing.world(player_position=player.position, player_direction=player.angle)
            drawing.mini_map(player)

            pygame.display.flip()  # обновление содержимого приложения
            clock.tick(FPS)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.btn_levels = wx.Button(self, wx.ID_OK, 'Уровни', (int(WIDTH / 2) - 100, int(HEIGHT / 2) - 70), (200, 70), )
        self.Bind(wx.EVT_BUTTON, self.on_levels, self.btn_levels)

    def on_levels(self, event):
        main_frame.Show(False)
        levels_frame.Show(True)
        levels_frame.Centre()


app = wx.App(False)
main_frame = Frame(None, 'Игра \"Лабиринт\"')
main_panel = MainPanel(main_frame)
levels_frame = Frame(None, 'Игра \"Лабиринт\": уровни')
levels_panel = LevelsPanel(levels_frame, 5)
main_frame.Show()
main_frame.Centre()
app.MainLoop()

# основной цикл
