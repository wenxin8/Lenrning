"""
sn = 1 + 1/2 + 1/3 + ... + 1/n
给出整数k,计算出最小的n,是得sn > k
"""
k = int(input())
sn = 0
n = 1
while n > 0:
    sn = sn + 1 / n
    if sn > k:
        break
    n = n + 1
print(n)
    
