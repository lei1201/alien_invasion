#！/usr/bin/env python
# -*- coding:utf-8 -*-
# _time_='2021/10/27 13:58'
# _PROJECT_NAME_=' alien_invasion '
# _NAME_=' alien_invasion '
# _USER_=' ThinkPad E15 '

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """用于初始化游戏"""
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.scree_width,ai_settings.scree_hight))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events()

        #每次循环都会重绘屏幕
        #让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship)

run_game()