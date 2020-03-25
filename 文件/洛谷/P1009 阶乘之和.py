"""
计算1! + 2! + 3! + ... + n!的和
"""
n = int(input())
sum0 = 0
for i in range(1, n + 1):
    j = i
    t = 1
    while j >= 1:
        t = t * j
        j = j - 1
    sum0 = sum0 + t
print(sum0)
