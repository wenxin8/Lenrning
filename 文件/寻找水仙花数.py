"""
1. 寻找**水仙花数**。
    > **说明**：水仙花数也被称为超完全数字不变数、自恋数、自幂数、
    阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好
    等于它本身，例如：1^3 + 5^3+ 3^3=153。
"""
for num in range(100, 1000):
    low = num % 10    # 153 % 10 = 3
    mid = num // 10 % 10    # 153 // 10 % 10 = 15 % 10 = 5
    high = num // 100    # 153 // 100 = 1
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num, end='  ')
    
