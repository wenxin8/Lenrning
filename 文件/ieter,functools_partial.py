# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:54:54 2020

@author: zhong
"""
from functools import partial
newinput = partial(input, '输入：\n')
    


a =list()
for line in iter(newinput, 'end'):
    a.append(line)
print(''.join(a))
    

