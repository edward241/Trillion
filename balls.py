from random import randint
from settings import Settings
import pygame

class Ball:
    def __init__(self):
        self.setting = Settings()
        self.ball_speed = self.setting.ball_speed
        # self.ball = pygame.draw.circle(screen,self.setting.ball_color,(600,400),self.setting.ball_r)
        # self.rect = self.ball.get_rect()

        self.new = (self.setting.screen_width/2,self.setting.screen_height/2)
        self.directs = [(-1, -1),(-1, 1),(1, -1),(1, 1)]
        self.left_up = self.directs[0]
        self.left_down = self.directs[1]
        self.right_up = self.directs[2]
        self.right_down = self.directs[3]
        index = randint(1,2)
        self.direct = self.directs[index-1]

    def new_init(self):
        """初始化"""
        self.new = (self.setting.screen_width / 2, self.setting.screen_height / 2)
        self.direct = self.directs[randint(1,1)-1]

    def update(self):
        """"""

        if self.direct == self.left_up and (self.new[0]<0 and self.new[1]>0):
            self.direct = self.right_up
        if self.direct == self.left_up and (self.new[0]>0 and self.new[1]<0):
            self.direct = self.left_down

        if self.direct == self.left_down and (self.new[0]<0 and self.new[1]>0):
            self.direct = self.right_down
        if self.direct == self.left_down and (self.new[0]>0 and self.new[1]>self.setting.rect_location_height):
            self.direct = self.left_up

        if self.direct == self.right_up and (self.new[0]>0 and self.new[1]<0):
            self.direct = self.right_down
        if self.direct == self.right_up and (self.new[0]>self.setting.screen_width and self.new[1]>0):
            self.direct = self.left_up

        if self.direct == self.right_down and (self.new[0]>self.setting.screen_width and self.new[1]>0):
            self.direct = self.left_down
        if self.direct == self.right_down and (self.new[0]>0 and self.new[1]>self.setting.rect_location_height):
            self.direct = self.right_up


        self.new_x = self.new[0] + (self.direct[0] * self.ball_speed)
        self.new_y = self.new[1] + (self.direct[1] * self.ball_speed)
        self.new = (self.new_x,self.new_y)


    def draw_ball(self,screen):
        pygame.draw.circle(screen, self.setting.ball_color, self.new , self.setting.ball_r)



