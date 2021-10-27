#！/usr/bin/env python
# -*- coding:utf-8 -*-
# _time_='2021/10/27 16:36'
# _PROJECT_NAME_=' alien_invasion '
# _NAME_=' game_gunctions '
# _USER_=' ThinkPad E15 '

import sys
import pygame

def check_events():
    """响应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()