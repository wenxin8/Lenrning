# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:03:56 2020

@author: zhong
"""
l = input().split()
n = float(l[0])
k = float(l[1])
countA = 0
a = 0
countB = 0
b = 0
for i in range(1, int(n)+1):
    if i % k == 0:
        countA +=  i
        a += 1
    else:
        countB +=  i
        b += 1
sA = round(countA / a, 1)
sB = round(countB / b, 1)
print(str(sA) + ' ' + str(sB) )

