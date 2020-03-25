n = int(input())
a = 0
for i in range(0, n):
    for j in range(0, n - i):
        a = a + 1
        print("{:0>2d}".format(a), end="")
    print()


"""
n = int(input())
line = n
a = 1
for i in range(n):
    for x in range(line):
        print("%.2d"%a,end='')
        a += 1
    line -=1
    print("")
"""
