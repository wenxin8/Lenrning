# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:47:42 2020

@author: zhong
"""
def r(x, y):
    counts = 0
    r = []
    for i in range(x, y + 1):
        if (i % 4 == 0 and i % 100 != 0) or (
                i % 400 == 0):
            counts += 1
            r.append(str(i))
    print(counts)    
    print(" ".join(r))
            
x, y = map(int,input().split())
r(x, y)       
            
            

