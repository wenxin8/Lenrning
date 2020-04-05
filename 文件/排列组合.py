
"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
def main():
    numbers = [1, 2, 3, 4]
    for i in numbers:
        one = i
        for j in numbers:
            two = j
            for k in numbers:
                three =k
                if i != j and i != k and j != k:
                    #if i <= j <= k:
                    print(i, j, k)

'''
从 n 个数1, 2, 3, 4, ..., n里抽出 r 个元素，输出所有组合
'''
def dfs(k):
    if (k > r ):
        for j in range(1, r + 1):
            print("%3d" % a[j], end='' )
        print()
        return
    #i = a[k - 1] + 1
    #while i < n + 1:
    #   a[k] = i
    #   dfs(k + 1)
    #   i = i + 1
    for i in range(a[k - 1] + 1, n + 1):
        a[k] = i
        dfs(k + 1)
def main1():
    global n, r, a
    n, r = map(int, input().split())
    a=['']*50
    a[0]=0
    dfs(1)
main1()



