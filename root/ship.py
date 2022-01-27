import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('photo/ship.png') # photo/ship.png # /Users/chenzhiyu/vscodeProjects/Alien_Invasion/photo/ship.png
        self.rect = self.image.get_rect()   # 使得图片为矩形， 得到 surface属性
        self.screen_rect = screen.get_rect()    # 将矩形存储到 该方法中
        # 与下两句组合成为下方中间； 起始(0,0)为左上角
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom  # 可能是固定用法，self.rect.[*] 与 self.screen_rect.[*] 要保持一致 ： bottom/center/top/bottom / centerx/centery


    def blitme(self):
        self.screen.blit(self.image, self.rect)
