import pygame
import time
from plane_sprites import *


# 游戏前的倒计时三秒
def gamebefore():
    # 1.创建游戏前的窗口
    screen = pygame.display.set_mode(SCREEN_RECT.size)   # 游戏窗口是1000*1000   倒计时背景图片也是1000*1000
    # 2.创建游戏的时钟
    clock = pygame.time.Clock()
    # 3.绘制背景图像，3个步骤
    # 3.1 加载图像数据(把图片从硬盘中加载到内存上)  3.2 使用游戏屏幕对象调用blit方法(第一个参数是图像，第二个参数是图像的位置)，将图像绘制到制定位置 3.3 updata更新屏幕显示,否则看不到加载的图片
    daojishi3 = pygame.image.load("./image/DD3.png")
    screen.blit(daojishi3, (0, 0))  # 将图片的左上角放在窗口的(0,0)坐标处

    daojishi2 = pygame.image.load("./image/DD2.png")
    screen.blit(daojishi2, (0, 0))

    daojishi1 = pygame.image.load("./image/DD1.png")
    screen.blit(daojishi1, (0, 0))

    for dc in range(4):  # 游戏循环即游戏开始
        clock.tick(1)  # 可以指定循环体内部代码执行的频率1s 1次
        if dc == 0:
            screen.blit(daojishi3, (0, 0))  # 绘制倒计时图片3
            pygame.display.update()
        if dc == 1:
            screen.blit(daojishi2, (0, 0))
            pygame.display.update()
        if dc == 2:
            screen.blit(daojishi1, (0, 0))
            pygame.display.update()

        for event in pygame.event.get():  # 根据事件作出动作，退出事件，并防止pygame窗口卡死
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


class PlaneGame(object):
    def __init__(self):
        # print("游戏初始化")
        # 1.创建游戏的窗口
        self.surface = pygame.display.set_mode(SCREEN_RECT.size)   # 游戏窗口是1000*1000   背景图片是1000*2291
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4.设置定时器事件, 创建敌机 每隔1s定时器触发一次事件(出现敌机), 每隔0.5s发射一次子弹
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        self.choice = GameSprite("./image/choice.png", 0)

    def __create_sprites(self):   # 创建精灵
        # 1.加载背景图片和创建背景图片组对象
        bg1 = BackGround()              # 加载第一张背景图片  游戏窗口是1000*1000   背景图片是1000*2291
        bg2 = BackGround(True)          # 加载第二张背景图片,传入True参数, 则表示交替图像
        self.background_group = pygame.sprite.Group(bg1, bg2)    # 添加两张图片到图片组并创建背景图片组对象，方便调用精灵组方法，可以有多个精灵组对象

        # 2.创建敌机的图片组对象
        self.enemy_group = pygame.sprite.Group()

        # 3.创建飞机的图片组对象,并添加到飞机图片组，因为需要对飞机和敌机进行碰撞检测，所以需要对飞机设计成属性
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 4.创建爆炸图的组对象
        self.boom_group = pygame.sprite.Group()

    def start_game(self):
        print("game begin")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(TIME)

            # 2.事件监听
            self.__event_hander(self)

            # 3.碰撞检测
            self.__check_collide()

            # 4.更新/绘制精灵组
            self.__update_sprites()

            # 5.更新图像显示
            pygame.display.update()

    @staticmethod
    def __event_hander(self):
        for event in pygame.event.get():     # 监听事件并作出动作，退出事件，并防止pygame窗口卡死
            if event.type == pygame.QUIT:
                print("你的分数是 %d" % (Enemy.SCORE - Enemy.flyingenemy))
                PlaneGame.__game_over(self)
            elif event.type == CREATE_ENEMY_EVENT:   # 对定时器事件的监听，当监听到定时器事件时，做出响应动作
                # print("敌机出现")
                # 1.创建敌机精灵
                enemy = Enemy()
                # 2.创建爆炸图精灵
                boom = Boom()
                # 3.设置爆炸的位置
                boom.rect.centerx = enemy.rect.centerx
                boom.rect.centery = enemy.rect.centery
                boom.speed = enemy.speed
                # 4.将爆炸精灵添加到爆炸组精灵
                self.boom_group.add(boom)
                # 5.将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()                    # 调用飞机的fire方法
            # 第一种获取按键的方法
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     self.hero.rect.x += 2
        # 第二种使用键盘提供的方法获取按键 - 返回的是按键元组
        keys_press = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值 为1则表示被按下
        if keys_press[pygame.K_RIGHT]:
            self.hero.rect.x += 3       # 飞机向右移动
        elif keys_press[pygame.K_LEFT]:
            self.hero.rect.x -= 3       # 飞机向左移动

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullet_group, True, True)
        # 敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)      # 此时飞机无敌，此方法返回值是被飞机撞毁敌机的列表
        if len(enemies) > 0:
            self.hero.kill()
            print("你的分数是 %d" % (Enemy.SCORE - Enemy.flyingenemy))
            self.Choice()

    def __update_sprites(self):   # 这里面的update顺序有很大关系，即是先绘制背景图片，再绘制敌机图片，再绘制英雄图片

        self.background_group.update()              # 将背景图片组中的所有图片调用update方法 即bg1和bg2 .update 向下移动
        self.background_group.draw(self.surface)    # 将背景图片组中的图片绘制在游戏的窗口上  默认左上角对齐 所以在之前需要修改图片的y值

        self.boom_group.update()
        self.boom_group.draw(self.surface)

        self.enemy_group.update()                   # 所有的敌机图片调用update方法，即向下移动
        self.enemy_group.draw(self.surface)         # 将敌机图片组中的图片绘制在游戏的窗口上 默认左上角对齐 所以在之前需要修改图片的y值或者x值

        self.hero_group.update()                   # 所有的英雄飞机图片调用update方法，即向下移动
        self.hero_group.draw(self.surface)         # 将英雄飞机图片组中的图片绘制在游戏的窗口上 默认左上角对齐 所以在之前需要修改图片的y值或者x值

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.surface)

    def Choice(self):
        # 1.加载选择图像,并显示在屏幕上
        while True:
            self.clock.tick(TIME)
            choice = pygame.image.load("./image/choice.png")
            self.surface.blit(choice, (0, 0))  # 将图片的左上角放在窗口的(0,0)坐标处
            pygame.display.update()
            keys_press = pygame.key.get_pressed()
        # # 2.如果选择enter则继续倒计时游戏
            if keys_press[pygame.K_RETURN]:         # 选择继续游戏
                gamebefore()
                game1 = PlaneGame()
                game1.start_game()
        # 3.如果选择end则退出游戏
            elif keys_press[pygame.K_ESCAPE]:
                self.__game_over(self)
            for event in pygame.event.get():  # 根据事件作出动作，退出事件，并防止pygame窗口卡死
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    @staticmethod
    def __game_over(self):
        print("game over")
        pygame.quit()
        exit()


if __name__ == '__main__':
    gamebefore()
    game = PlaneGame()
    game.start_game()


