# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:57:14 2020

@author: zhong
"""
  # 计算n的阶乘 n!
  # 递归
def jc(x):
    if x == 0:
        return 1
    return x * jc(x - 1)

n = int(input())
print(jc(n))

