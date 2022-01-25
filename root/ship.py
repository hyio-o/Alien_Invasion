import pygame
class Ship():
    def __init__(self, screen):
        self.screen = screen    # 初始化飞船
        self.image = pygame.image.load('../photo/ship.png') # 加载飞船
        self.rect = self.image.get_rect()   # 获取外接矩形
        self.screen_rect = screen.get_rect() # TODO (不是很懂, screen 不是属于变量吗,怎么可以用方法?)
        # 讲每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.image, self.rect) # 在指定位置绘制飞船