import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """表示飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将飞船放置在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志（飞船一开始不移动）
        self.moving_right = False
        self.moving_left = False

        # 在飞船的属性xy中存储一个浮点数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的x值，而不是rect对象
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # 更新rect对象的位置
        self.rect.x = self.x


    def center_ship(self):
        # 将飞船放置在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)