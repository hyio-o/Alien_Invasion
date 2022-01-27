import sys
import pygame
from ship import Ship
from settings import Settings


ai_st = Settings()  # 要使用,应该先赋予其类 (类赋予)
screen = pygame.display.set_mode((ai_st.screen_width, ai_st.screen_height))
ship = Ship(screen)

# 响应按键与鼠标事件
"""每当用户按键时，都将在Pygame中注册一个事件。事件都是通过方法pygame.event.get() 获取的，因此在函数check_events() 中，我们需要指定要检查哪些类型的事件。每次按键都被注册为一个KEYDOWN 事件。

检测到KEYDOWN 事件时，我们需要检查按下的是否是特定的键。例如，如果按下的是右箭头键，我们就增大飞船的rect.centerx 值，将飞船向右移动："""
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 按下按键反应
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1      # 右键则飞船向右移动
            """elif event.key == pygame.K_LEFT:
                ship.rect.centery += 1
            elif event.key == pygame.K_UP:
                ship.rect.centery = 0"""


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
