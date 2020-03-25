# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:20:35 2020

@author: zhong
"""
#split()当不带参数是以空格进行切割
s = 'have dinner'
print(s.split())

#以'.'为分隔符
s = 'www.baidu.com'
print(s.split('.'))

#分割一次
print(s.split('.',1))

#分割两次，取第一个分片(序号为0)
print(s.split('.',2)[0])

#分割两次，并把分割后的三个部分保存到三个变量中
v1, v2, v3 = s.split('.')
print(v1, v2, v3)

v1, v2, v3 = s.split('.', 2)
print(v1, v2, v3)
'''
n = input("qing shu ru liang ge shu zi : ").split()
print(int(n[0]) + int(n[1]))

'''