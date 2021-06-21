import pygame
from settings import Settings
from balls import Ball
from rect import Recta
from button import Button
import game_function as gf
from status import GameStats
from scoreboard import ScoreBoard
import sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    pygame.display.set_caption('balls')
    setting = Settings()
    ball = Ball()
    rect = Recta()
    play_button = Button(setting, screen, "Play")
    status = GameStats(setting)
    sb = ScoreBoard(setting,screen,status)
    while True:

        gf.check_events(setting, screen, status, sb, play_button, ball,rect)

        if status.game_active:
            ball.update()
            rect.update()
            gf.check_result(setting,ball,rect,status,sb)
        print(sb.stats.level)
        gf.update_screen(setting, screen, status, sb, ball,rect,play_button)




run_game()
