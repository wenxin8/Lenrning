a = int(input())
s = 1
for i in range(1, a + 1):   # 行
    for j in range(1, a + 1):   # 列
        print("%02d" % s, end='')
        s = s + 1
    print()
print()
s = 1
for i in range(1, a + 1):   # 行
    for j in range(1, a + 1):   # 列
        if j <= (a - i):
            print(' ', end = ' ')
        else:
            print("%02d" % s, end='')
            s = s + 1
    print()
        

        
    
