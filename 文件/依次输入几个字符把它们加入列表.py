i = 5
j = 1
string = []
while i > 0 :
    temp = input("请输入第" + str(j) + "个字符")
    n = str(temp)
    string.append(n)
    j = j + 1
    i = i - 1
else :
    print(string)
    
