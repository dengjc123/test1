#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from test1.model1 import ClassA1
#
# c=ClassA1() # 赋值
# c.a()   #调用ClassA1中  a() 输出方法

class Product():
    size="6 inc"
    def __init__(self,color):
        self.color=color

    def call(self):
        print("hello")
    def message(self):
        print("我，秦始皇，打钱")

#实例化
phone = Product("white")

#获取属性
print(phone.color)
print(phone.size)
#调用方法
phone.message()
phone.call()
