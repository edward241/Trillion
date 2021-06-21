import sys
from time import sleep

import pygame

def ball_move():
    """"""




def rect_move():
    """"""



def check_events(setting, screen,status, sb, play_button,ball, rect):
    """"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rect)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rect)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(setting, screen,status, sb, play_button,ball,rect, mouse_x, mouse_y)

def check_keydown_events(event,rect):
    """按下"""
    if event.key == pygame.K_RIGHT:
        rect.moving_right = True
    elif event.key == pygame.K_LEFT:
        rect.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,rect):
    """按下"""
    if event.key == pygame.K_RIGHT:
        rect.moving_right = False
    elif event.key == pygame.K_LEFT:
        rect.moving_left = False

def check_play_button(settings,screen,status, sb, play_button, ball,rect, mouse_x, mouse_y):
    """"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not status.game_active:
        # Reset the game settings.
        settings.initialize_dynamic_settings()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        status.reset_stats()
        status.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        ball.draw_ball(screen)
        rect.draw_rect(screen)


def update_screen(setting, screen, status, sb, ball,rect,play_button):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(setting.bg_color)

    # Redraw all bullets, behind ship and aliens.
    ball.draw_ball(screen)
    rect.draw_rect(screen)

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not status.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def check_edge(ball,rect):
    """检测碰撞，ball的横坐标在rect内"""
    if rect.new_x > ball.new_x or ball.new_x > rect.new_x+rect.width:
        return False
    else:
        return True



def check_result(setting,ball,rect,status,sb):

    if ball.new[1] == setting.rect_location_height:
        re = check_edge(ball,rect)
        if re:
            status.score += setting.point
            sb.prep_score()
            check_level_up(status,setting,ball,rect,sb)
            if status.score > status.high_score:
                status.high_score = status.score
                sb.prep_high_score()
        else:
            status.reset_stats()
            ball.new_init()
            rect.new_init()
            another_game(status)



def another_game(status):
    """Respond to ship being hit by alien."""

    status.game_active = False
    pygame.mouse.set_visible(True)

    # Pause.
    sleep(0.5)


def check_level_up(status,setting,ball,rect,sb):
    if (status.score > 500 and setting.level==1) or (status.score > 1000 and setting.level ==2)\
            or (status.score > 1500 and setting.level==3) or (status.score > 2000 and setting.level==4) :
        setting.level_up()
        ball.ball_speed = setting.ball_speed
        rect.width = setting.rect_width
        print('level up')
        sb.prep_level()

