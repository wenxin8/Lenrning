count = 0
m = [1, 2, 3, 4]
for a in m:
    for b in m:
        for c in m:
            if a != b and b != c and a != c:
                count = count + 1
                print ("%d %d %d" % (a, b, c))
print("能组成%d个不相同且无重复的3位数" % count)

                