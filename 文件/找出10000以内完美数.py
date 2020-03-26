"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""
import math
for num in range(1,10000):
    # n的因子x，y
    m = []
    for x in range(1, int(math.sqrt(num)) + 1):   
        if num % x == 0:
            m.append(x)
            if (num / x) != x and (num / x) != num:
                m.append(num / x)
        
    if num == sum(m):
        print(num)

                
