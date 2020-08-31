#!/usr/bin/python3       添加这行 可在linux终端下执行python代码的文件  直接./example1.py
# -*- coding: UTF-8 -*-    在python2中可支持中文字符
import time
import random  #random.randint
# import test1
# a=test1.xyh('5','3')

#           例子1：摆放家具------------------------类的定义与使用


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return ("家具名称是 %s,占地面积是 %0.1f" %(self.name,self.area))

class House:
    def __init__(self,house_type,area):
        self.area=area
        self.freearea=area
        self.house_type=house_type
        self.item=''

    def __str__(self):
        return ("户型是 %s, 总面积是 %d, 剩余面积是 %0.1f,家具名称列表是 %s" %(self.house_type,self.area,self.freearea,self.item))

    def add_item(self,item):
        if self.freearea>item.area:
            self.freearea=self.freearea-item.area
            self.item+=item.name
        else:
            print("can't add %s" %item.name)

bed=HouseItem(" 席梦思",4)
chest=HouseItem(" 衣柜",2)
table=HouseItem(" 餐桌",1.5)
big_bed=HouseItem(" 大床",200)
print(bed)
print(chest)
print(table)

xyh=House("别墅",120)
xyh.add_item(bed)               # 一个类的对象可以作为另一个类的方法的实参传入，进而再使用该类的属性或方法
xyh.add_item(chest)
xyh.add_item(table)
xyh.add_item(big_bed)
print(xyh)


#           例子2：士兵突击------------------------
class Gun:
    def __init__(self,model):
        self.model=model
        self.bullet_count=0

    def add_bullet(self,count):
        self.bullet_count+=count

    def shoot(self):
        if self.bullet_count>0:
            self.bullet_count-=1
            print("you are shooting now ,remain bullet are %d" %self.bullet_count)
        else:
            print("there is no bullet")


class Soldier:
    def __init__(self,name):
        self.name=name
        self.gun=None
    def fire(self):
        if self.gun is None:
            print("you have not gun")
        else:
            self.gun.add_bullet(6)
            self.gun.shoot()

AK=Gun("AK47")
xyh=Soldier("许三多")
xyh.gun=AK     # important-------------一个类的对象可以是另一个类的属性
xyh.fire() 
