'''
n = int(input())
a = input().split()
b = [int(i) for i in a ]
b.sort()
print(b[0])
'''


n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0])


'''
n = int(input())
a = input().split()
for m in range(0, len(a)):
    a[m] = int(a[m])
a.sort()
print(a[0])
'''
