"""题目描述
试计算在区间1到n的所有整数中，数字 x(0≤x≤9)
共出现了多少次？例如,在1到11中，
即在 1,2,3,4,5,6,7,8,9,10,11中，数字1出现了44次。
样例：
输入 11 1
输出 4
"""

n, x = map(int, input().split())
c = 0
for a in range(1, n + 1):
    c = c + str(a).count(str(x))
print(c)


"""
n, x = map(int, input().split())
s =''
for a in range(1, n + 1):
    s = s + str(a)
print(s.count(str(x)))
"""
