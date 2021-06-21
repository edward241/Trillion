import pygame
from settings import Settings
class Recta:
    def __init__(self):
        self.setting = Settings()

        self.rect_height = self.setting.screen_height * 9 / 10
        # self.orgin = (self.setting.screen_width/2,)
        # print(self.orgin)
        self.new = (self.setting.screen_width/2, self.rect_height)
        self.new_x = self.new[0]
        self.width = self.setting.rect_width
        self.moving_left = False
        self.moving_right = False

    def new_init(self):
        """"""
        self.new = (self.setting.screen_width / 2, self.rect_height)

    def update(self):
        """"""
        if self.new[0] > 0 and self.moving_left:
            self.new_x = self.new[0] - (self.setting.level * self.setting.rect_speed)
        elif self.new[0]+ self.setting.rect_width < self.setting.screen_width and self.moving_right:
            self.new_x = self.new[0] + (self.setting.level * self.setting.rect_speed)
        else:
            self.new_x = self.new[0]
        self.new = (self.new_x,self.rect_height)


    def draw_rect(self,screen):
        pygame.draw.rect(screen, self.setting.rect_color, (self.new_x, self.rect_height, self.width, self.setting.rect_height))