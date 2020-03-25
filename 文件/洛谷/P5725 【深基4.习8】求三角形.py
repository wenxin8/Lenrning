a = int(input())
s = 1
for i in range(0, a):
    for j in range(0, a):
        print("%02d" % s, end='')
        s = s + 1
    print()
print()
s = 1
for i in range(0, a):
    for j in range(0, a ):
        if j < (a -1 - i):
            print(' ', end = ' ')
        else:
            print("%02d" % s, end='')
            s = s + 1
    print()
        

        
    
