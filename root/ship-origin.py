import pygame
class Ship():
    def __init__(self, screen):
        self.screen = screen    # 初始化飞船
        self.image = pygame.image.load('../photo/ship.png') # 加载飞船 ; pygame.image.load()  这个函数返回一个表示飞船的surface，而我们将这个surface存储到了self.image 中。
        self.rect = self.image.get_rect()   # 获取外接矩形 ; get_rect() 获取相应surface的属性rect;; 处理rect 对象时，可使用矩形四角和中心的 x 和 y 坐标。可通过设置这些值来指定矩形的位置。

        self.screen_rect = screen.get_rect() # TODO (不是很懂, screen 不是属于变量吗,怎么可以用方法?)
        # 讲每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        # 可设置相应rect 对象的属性center 、centerx 或centery 。要让游戏元素与屏幕边缘对齐，可使用属性top 、bottom 、left 或right ；要调整游戏元素的水平或垂直位置，可使用属性x 和y ，它们分别是相应矩形左上角的 x 和 y 坐标。
        self.rect.bottom = self.screen_rect.bottom
        """我们将把飞船放在屏幕底部中央。为此，首先将表示屏幕的矩形存储在self.screen_rect 中（见❸），再将self.rect.centerx （飞船中心的x 坐标）设置为表示屏幕的矩形的属性centerx （见❹），并将self.rect.bottom （飞船下边缘的y 坐标）设置为表示屏幕的矩形的属性bottom 。"""
        """注意 　在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。在1200×800的屏幕上，原点位于左上角，而右下角的坐标为(1200, 800)。"""
    def blitme(self):
        self.screen.blit(self.image, self.rect) # 在指定位置绘制飞船
