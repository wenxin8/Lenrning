"""
给定一个整数，请将该数各个位上数字反转得到一个新数
例如：输入123 输出321
     输入-380 输出-83
"""
n = int(input())
if n > 0:
    new = str(n)[::-1]
    print(int(new))
else:
    new = str(abs(n))[::-1]
    print(0 - int(new))
