#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import  json
# j='''{"name":"stu","age":18}'''
#
# z=json.loads(j)
# print(z)
#
# j=json.dumps(z)
# print(j)

# import  random
# a = random.randint(1,20)
# print(a)
#
# c= random.choice([1,2,3,4,8]) #可输入字符串 元组 列表
# print (c)
#
# import os
# p = os.path.abspath("open.text")
# print(p)
# d = os.path.dirname(p)
# print(d)
# f = os.path.basename(p)
# print(f)
#
# m = os.path.abspath(__file__) #定义当前文件的绝对路径  model1
# print (m)
#
# os.system("ipconfig")
import os
try:
    os.mkdir("test1")
except:
    print("已经存在了")
else:
    print("创建成功")
finally:
    print("欢迎下次光临")

print(123,"修改")

