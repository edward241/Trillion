from random import randint


class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ball_color = (255,0,0)
        self.rect_color = (0,255,0)

        self.ball_speed = 1
        self.rect_speed = 1

        self.ball_r = 10  # 半径
        self.rect_width = 300  #  长度
        self.rect_height = 20
        self.rect_location_height = self.screen_height * 9/10

        self.level = 1

    def initialize_dynamic_settings(self):
        """初始化"""
        self.level = 1
        self.point = 50

    def level_up(self):
        """"""

        self.rect_width -= 10
        self.ball_speed *= 1.05


