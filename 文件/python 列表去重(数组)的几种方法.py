  # 方法1 思路看起来比较清晰简单 ，也可以保持之前的排列顺序。
ids = [1, 2, 3, 2, 1, 4, 5, 6, 4]
new_ids = []
for i in ids:
    if i not in new_ids:
        new_ids.append(i)
print(new_ids)

  # 方法2 通过set方法进行处理
  # 处理起来比较简单，使用了集合方法set进行处理，不过结果不会保留之前的顺序。
ids = [1,4,3,3,4,2,3,4,5,6,1]
ids = list(set(ids))
print(ids)

  # 使用itertools模块
import itertools
ids = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
ids.sort()

  # itertools.groupby()就是将相邻的并且相同的键值划分为同一组
it = itertools.groupby(ids)
new_ids = []
for k, g in it:
    new_ids.append(k)
print(new_ids)
