import sys
import pygame


def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()   # 初始化背景设置
    screen = pygame.display.set_mode((1200, 800))  # 实参(1200, 800) 是一个元组，因而需要两个括号
    # 对象screen 是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个surface。
    pygame.display.set_caption("Alien Invasion")
    # 游戏主循环
    while True:
        # 监视 键鼠 事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 最近绘制屏幕可见
        pygame.display.flip()  # 命令Pygame让最近绘制的屏幕可见。在这里，它在每次执行while 循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。
        # 将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果。

run_game()
