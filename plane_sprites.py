import random
import pygame

# 游戏屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 1000, 1000)  # 记录矩阵的数值的x, y, width, height   默认图片与屏幕的左上角对齐
# 刷新帧率
TIME = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建英雄发射子弹的定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):     # 图片类  其下有背景图片对象,飞机图片对象, 敌机图片对象, 子弹图片对象,他们均是图片类的派生对象
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()    # image的get_rect方法,可以返回 pygame.Rect(0,0,图像宽,图像高)的对象 即默认把图片放在左上角
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):       # 背景图片类
    def __init__(self, is_alt=False):
        super().__init__("./image/background.png")  # 调用父类的init方法同时给image_name值初始化
        if is_alt:
            self.rect.y = -self.rect.height    # 如果传入的is_alt参数为真，则将图片放在屏幕的上方,y值为背景图片的高度-1000(不设置的话默认y值是0),然后一起向下滚动

    def update(self):               # 拓展图片类的update方法，实现背景图片的向下移动----(两张背景图片向下移动)
        super().update()
        if self.rect.y >= SCREEN_RECT.height:       # 如果图片移出了屏幕，则返回到屏幕的上方再次滚动
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):           # 敌机图片类
    SCORE = 0
    flyingenemy = 0

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./image/enemy4.png")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(2, 4)
        # 3.指定敌机的初始随机位置x和初始y值
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)   # 屏幕宽度减去敌机图片的宽度
        self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类方法，保持垂直方向上的飞行
        super().update()
        # 2.判断敌机是否飞出屏幕，如果飞出，则从图片组删除敌机图片对象，释放内存
        if self.rect.y >= SCREEN_RECT.height:
            Enemy.flyingenemy += 1
            self.kill()         # 将精灵从所有精灵组中删除，精灵就会被自动销毁  销毁前调用__del__方法

    def __del__(self):
        Enemy.SCORE += 1


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./image/plane.png", 0)
        # 设置飞机的初始位置
        self.rect.centerx = SCREEN_RECT.centerx    # 利用Rect的属性centerx和Buttom来设置飞机的初始位置   两张图片的中心x处对齐
        self.rect.y = SCREEN_RECT.bottom - 200          # centerx 即图片的中心x处    buttom = y + height  离下屏幕边框200
        # 创建子弹精灵组属性
        self.bullet_group = pygame.sprite.Group()

    def update(self):       # 重写update方法，禁止飞机飞出屏幕   飞机图片131*175  屏幕1000*1000
        if self.rect.right >= SCREEN_RECT.width:        # right = x + width
            self.rect.right = SCREEN_RECT.width
        elif self.rect.x <= 0:
            self.rect.x = 0

    def fire(self):
        # 1.创建子弹精灵
        bullet = Bullet()
        # 2.设置子弹精灵的位置
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.y
        # 3.将子弹添加到子弹精灵组
        self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./image/bullet1.png", -2)

    def update(self):
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        pass
        # print("子弹被销毁")


class Boom(GameSprite):
    def __init__(self):
        super().__init__("./image/boom1.png")

    def update(self):
        super().update()

