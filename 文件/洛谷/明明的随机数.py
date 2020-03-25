#输入随机数的个数
import random
n = input()
a = input().split()
b = []
for id in a:
    if id not in b:
        b.append(id)
print(len(b))
for i in range(0, len(b)):
    for j in range(i + 1, len(b)):
        if int(b[i]) > int(b[j]):
            b[i], b[j] = b[j] , b[i]
for k in range(0, len(b)):
    print(b[k], end=' ')
