#!/usr/bin/python3       添加这行 可在linux终端下执行python代码的文件  直接./example1.py
# -*- coding: UTF-8 -*-
import time
import random  # random.randint
# import test1
# a=test1.xyh('5','3')

#           -------------------1.方法综合
class Game(object):
    top_score = 0

    def __init__(self, player_name):   # 创建了初始化方法
        self.player_name = player_name

    def start_game(self):               # 实例方法 参数self
        print("%s 开始游戏啦" % self.player_name)

    @staticmethod
    def show_help():                    # 静态方法无参数
        print("帮助信息F1")

    @classmethod
    def show_top_score(cls):            # 类方法 参数cls
        print("历史最高分是 %d" % cls.top_score)


Game.show_help()
Game.show_top_score()
tcs = Game("xyh")
tcs.start_game()


#           --------------------2.new方法的重写
class Method(object):
    def __init__(self):
        print("对象的初始化")

    def __new__(cls, *args, **kwargs):
        print("分配内存空间")
        return super().__new__(cls)     # 返回对象的引用(必须添加，否则不会调用init方法)


method=Method()             # 1.调用new方法为对象分配内存   2.调用init方法初始化对象
print(method)               # 调用str方法，打印对象的内存地址


#       ------------------------3.编写单例设计模式
class Method(object):
    count = -1
    lei_count = None        # 定义两个类属性

    def __init__(self):
        print("对象的初始化")

    def __new__(cls, *args, **kwargs):
        print("分配内存空间")
        Method.count+=1
        if Method.count<1:
            Method.lei_count=super().__new__(cls)       # 用类属性记录对象的引用，第二次调用对象时不再调用父类的new方法，即不会再开辟新的内存空间
        return  Method.lei_count


method1=Method()
print(method1)
method2=Method()
print(method2)              # 此时两个对象的内存地址一样，为单例设计模式


#       -------------------------4.只执行一次初始化动作(但还是会每次都调用init函数，只是里面的动作只执行一次)
class Method(object):
    count = -1
    lei_count = None
    init_count = -1             # 再定义一个类属性

    def __init__(self):
        Method.init_count += 1
        if Method.init_count == 0:
            print("对象的初始化")         # if判断语句  只执行一次动作，后面的对象创建时不再执行

    def __new__(cls, *args, **kwargs):
        print("分配内存空间")
        Method.count += 1
        if Method.count < 1:
            Method.lei_count=super().__new__(cls)
        return  Method.lei_count


method1 = Method()
print(method1)
method2 = Method()
print(method2)

#     -----------------5.异常的完整语法
try:
    a = int(input("a number: "))
    b= 8/a
    print(b)
except ValueError:
    print("your number is not a num")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("no wrong")
finally:
    print("异常与否均会执行的代码")
print("-"*50)

#       ----------------6.主动抛出异常
def input_passwd():
    pwd = input("请输入密码： ")
    if len(pwd) >= 8:
        return pwd
    print("主动抛出异常")
    # 1.创建异常对象-可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 2.主动抛出异常
    raise ex

try:            # 抛出异常再捕获异常
    print(input_passwd())
except Exception as result:
    print(result) 
