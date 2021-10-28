#！/usr/bin/env python
# -*- coding:utf-8 -*-
# _time_='2021/10/27 15:13'
# _PROJECT_NAME_=' alien_invasion '
# _NAME_=' settings '
# _USER_=' ThinkPad E15 '

class Settings():
    """存储游戏中所有设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.scree_width = 1200
        self.scree_hight = 800
        self.bg_color = (230,230,230)

        #飞船的设置
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60,60,60