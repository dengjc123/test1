#!/usr/bin/env python
# -*- coding:utf-8 -*

#读写文件操作
#1、写入  绝对路径  也可以写绝对路径  "w" write "r" read 根据需求去填写
# 单\是转入 不是windows中目录符  所以需要添加另一个\来标识
'''a = open("D:\\softwaredate\\PycharmProjects\\test\\open.txt","w")
a.write("测试写入功能")
a.close()'''
# w 是清空写入  先清空内容 后写入
# a 文件内容后追加内容写入
'''a = open("D:\\softwaredate\\PycharmProjects\\test\\open.txt","a")
a.write("测试写入功能")
a.close()'''
# b 也是写入  用于二进制  表上传用  了解
#写入时  pycharm默认使用GBK 所以中文下读取是乱码 需转码如下
a = open("D:\\softwaredate\\PycharmProjects\\test\\open1.txt","w",encoding=("utf-8"))
#a.write("测试写入功能")  w写的是参数类型
# w lines写入类型是列表
a.writelines(["123456\n","789\n","是否"])
a.close()

#2、读取  open read  直接读取文件全部内容
# a = open("open1.txt","r",encoding=("utf-8"))
# b = a.read()
# print (b)
# a.close()
#按行读取文件全部内容  readlines
# a = open("open1.txt","r",encoding=("utf-8"))
# b = a.readlines()
# print (b)
# a.close()
#读取一行文件内容  readline
# a = open("open1.txt","r",encoding=("utf-8"))
# b = a.readline()
# c = a.readline()
# print (b,c)
# a.close()

#with  as   with后面跟操作语句  as 赋值 给变量 a
#这样可以不用最后加close  会更节省系统资源
with open("open1.txt","r",encoding=("utf-8")) as a:
    b=a.read()
    print(b)



