"""
计算 1+2+3+\cdots+(n-1)+n1+2+3+⋯+(n−1)+n 的值
"""
n = int(input())
su = 0
for i in range(1, n + 1):
    su = su + i
print(su)
