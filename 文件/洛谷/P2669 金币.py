"""
题目描述
国王将金币作为工资，发放给忠诚的骑士。
第一天，骑士收到一枚金币；之后两天（第二天和第三天），每天收到两枚金币；
之后三天（第四、五、六天），每天收到三枚金币；
之后四天（第七、八、九、十天），每天收到四枚金币……；
这种工资发放模式会一直这样延续下去：当连续N天每天收到N枚金币后，
骑士会在之后的连续N+1天里，每天收到N+1枚金币。
请计算在前K天里，骑士一共获得了多少金币。
输入 1000    输出 29820
输入 6       输出 14
"""
'''
思路
1
22
333
4444
.....
'''
k = int(input())
a = []
b = 0
for i in range(1, k + 1):
    if b == k:
        break
    else:
        for j in range(0, i ):
            a.append(i)
            b = b + 1
            if b == k:
                break
s = 0
for m in range(0, k):
    s = s + a[m]
print(s)
    
'''
x=int(input())
money=1
su=0
k=0
for i in range(x):
    su=su+money
    k=k+1
    if k==money:
        money=money+1
        k=0
print(su)
'''
