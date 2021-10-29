#！/usr/bin/env python
# -*- coding:utf-8 -*-
# _time_='2021/10/29 17:03'
# _PROJECT_NAME_=' alien_invasion '
# _NAME_=' game_stats '
# _USER_=' ThinkPad E15 '

class GameStatus():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_status()

    def reset_status(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit