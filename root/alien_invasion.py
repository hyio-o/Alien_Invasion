import sys
import pygame


def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))  # 实参(1200, 800) 是一个元组，因而需要两个括号
    pygame.display.set_caption("Alien Invasion")
    # 游戏主循环
    while True:
        # 监视 键鼠 事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 最近绘制屏幕可见
        pygame.display.flip()


run_game()
