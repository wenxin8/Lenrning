j = 1
while j < 10:  
    i = 1
    while i < j + 1:
        print("{}*{}={}".format(i, j, i*j), end="\t")
        i = i + 1
    print()
    j = j + 1

input()  #######
