#!/usr/bin/python3       添加这行 可在linux终端下执行python代码的文件  直接./example1.py
# -*- coding: UTF-8 -*-
import time
import random  #random.randint
# import test1
# a=test1.xyh('5','3')

#             ---------1.类的单继承
class Woman:
    def __init__(self):
        self.name="小颖"
        self.__age=18
    def __secret(self):
        print("my age is good")
    def hh(self):
        print("age is %d" % self.__age)
        self.__secret()

class ly(Woman):
    def dd(self):
        print("%s" % self.name)
        self.hh()           # 方法中调用另一个方法，进而间接访问父类的私有方法和私有属性

lxy=ly()
lxy.dd()


#         ----------------2.类的多继承
class A:
    def AA(self):
        print("AAA")


class B:
    def AA(self):
        print("BBB")
class C(B,A):
    def CC(self):
        print("CCC")
c=C()
c.AA()
print(C.__mro__)     # 方法搜索顺序


#         ----------------3.多态案例
class Dog():
    def __init__(self,name):
        self.name=name
    def game(self):
        print("%s" %self.name)

class Xiaotiandog(Dog):
    def game(self):
        print("%s" %self.name)

class Person():
    def __init__(self,name):
        self.name=name
    def game_with_dog(self,dog):
        print("%s 和 %s 玩耍" %(self.name,dog.name))
        dog.game()

# wangcai = Dog("旺柴")
wangcai = Xiaotiandog("飞天旺柴")
xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)


#       ----------------4.类属性与类方法
class Tool(object):
    count = 0
    @classmethod                 # 修饰符
    def show_tool_count(cls):
        print("数量为%d" %cls.count)       # 内部调用 cls.

    def __init__(self,name):
        self.name = name
        Tool.count+=1         # 对象方法中调用类属性： 类名.类属性

tool1=Tool("斧头")
tool2=Tool("榔头")
Tool.show_tool_count()


#     ---------------------5.静态方法
class Dog(object):
    @staticmethod           # 修饰符
    def run():
        print("小狗")


Dog.run()     # 调用方法时：   类名.静态方法

