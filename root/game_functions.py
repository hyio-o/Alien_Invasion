import sys
import pygame


# 响应按键与鼠标事件
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()


"""
类似与游戏主循环中的代码：
    while True:
        # 监视 键鼠 事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
"""
