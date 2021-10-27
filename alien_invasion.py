#！/usr/bin/env python
# -*- coding:utf-8 -*-
# _time_='2021/10/27 13:58'
# _PROJECT_NAME_=' alien_invasion '
# _NAME_=' alien_invasion '
# _USER_=' ThinkPad E15 '

import sys
import pygame

def run_game():
    """用于初始化游戏"""
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color = (230,230,230)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环都会重绘屏幕
        screen.fill(bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()