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
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    """用于初始化游戏"""
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    # 创建一个外星人编组
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏的主循环
    while True:

        gf.check_events(ai_settings,screen,ship,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()