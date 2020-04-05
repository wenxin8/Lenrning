import random
import string

# 随机整数,包括1,10
random.randint(1, 10)
# 从0开始的间隔2的随机数，也就是偶数，包括0到不包括100
random.randrange(0, 100, 2)
# 随机浮点数
random.random() # [0,1)的浮点数
random.uniform(1, 10)
random.uniform(10, 1) # random.uniforn(a,b) = a + (b-a) * random()中的浮点舍入，
                     # b可以包括或不包括在该范围
# 随机字符
random.choice('abcdefghigklmnopqrstuvwxyz!@#$%^&*()')
# 多个字符生成指定数量的随机字符，返回列表
random.sample('abcdefghijklmnopqrstuvwxyz', k = 5)
# 从a-zA-Z0-9生成指定数量的随机字符
ran_str = ''.join(random.sample(
    string.ascii_letters + string.digits, 8
))
# 多个字符中选取指定数量的字符组成新字符串
new_str = ''.join(random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's'], 5 ))
# 随机选取字符串
random.choice(['剪刀', '石头', '布'])

#打乱顺序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)

#返回随机数N， 1 <= N <= 10,  5默认中点，靠近哪一边，哪边权重更多多
random.triangular(1, 10)
random.triangular(1, 10, 3)

##random.choices(population, weights=None, *, cum_weights=None, k=1)
#从*population*中选择替换，返回大小为 k 的元素列表。 如果 population 为空，
# 则引发 IndexError。
#如果指定了 weight 序列，则根据相对权重进行选择。 或者，如果给出 cum_weights 序列，
# 则根据累积权重（可能使用 itertools.accumulate() 计算）进行选择。
# 例如，相对权重``[10, 5, 30, 5]``相当于累积权重``[10, 15, 45, 50]``。
# 在内部，相对权重在进行选择之前会转换为累积权重，因此提供累积权重可以节省工作量。
s1 = s2 = s3 = 0
for i in range(10000):
    a = random.choices([1, 2, 3], weights=[5, 3, 2], k = 1)
    if a[0] == 1:
        s1 += 1
    elif a[0] == 2:
        s2 += 1
    else:
        s3 += 1
print(f'[1]的个数：{s1}\n[2]的个数：{s2}\n[3]的个数：{s3}')


