import pygame
from pygame.locals import *
from plane_sprites import *
# 游戏框架搭建
# 1.游戏初始化(设置游戏窗口,创建游戏时钟,创建精灵和精灵组)
# 2.游戏循环(设置刷新帧率,事件监听,碰撞检测,更新/绘制精灵组,更新屏幕显示)

pygame.init()  # 第一步初始化方法
hero_rect = pygame.Rect(100, 500, 120, 125)  # 左上角坐标是(0,0)  此时初始图片左上角坐标为(100,500) 四个值分别是 x,y,width,height
print("%d %d" % (hero_rect.x, hero_rect.y))  # pygame.Rect类里有x.y.width,height,size属性
print("%d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)   # size属性是一个元组属性 分别返回的是矩形的宽度和高度

# 1.创建游戏的窗口 1024*1000 必须使用一个变量来记录返回的结果
surface = pygame.display.set_mode((1024, 1000))

# 2.绘制背景图像，3个步骤
# 2.1 加载图像数据(把图片从硬盘中加载到内存上)  2.2 使用游戏屏幕对象调用blit方法(第一个参数是图像，第二个参数是图像的位置)，将图像绘制到制定位置 2.3 updata更新屏幕显示,否则看不到加载的图片
bg = pygame.image.load("./image/background.png")
surface.blit(bg, (0, 0))     # 将图片的左上角放在窗口的(0,0)坐标处

# 3.绘制飞机图像224*300，3个步骤
plane = pygame.image.load("./image/plane2.png")
surface.blit(plane, (300, 700))
y = 700
pygame.display.update()  # 可以在所有绘制图像之后 统一调用一次update

# 4.创建时钟对象
clock = pygame.time.Clock()

# 5.创建精灵对象 即敌机对象
enemy = GameSprite("./image/enemy.png")
enemy1 = GameSprite("./image/enemy.png", 2)

# 创建敌机的图片组对象
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:    # 游戏循环即游戏开始

    clock.tick(60)   # 可以指定循环体内部代码执行的频率1s 10次
    event_list = pygame.event.get()   # 监听事件
    if event_list == []:
        pass
    else:
        print(event_list)
    y -= 2

    surface.blit(bg, (0, 0))            # 先重新绘制游戏图像，再绘制飞机图像，这样既可以遮挡之前绘制的图像又避免出现飞机图像刷新时的残影
    surface.blit(plane, (300, y))

    enemy_group.update()                # 精灵组调用的两个方法，分别是让组中所有精灵调用update方法(即向下移动)
    enemy_group.draw(surface)           # 让精灵的image绘制到屏幕对象的rect位置(0,0)

    pygame.display.update()

    if y == -300:
        y = 1000

    for event in pygame.event.get():  # 根据事件作出动作，退出事件，并防止pygame窗口卡死
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
