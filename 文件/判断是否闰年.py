#闰年判断
#能被4整除但不能被100整除,或者能被400整除都是闰年
while 1:
    temp = input("请输入你要判断的年份： ")
    n = int(temp)
    x1 = n % 4
    x2 = n % 100
    y = n % 400

    
    """
    if (x1 == 0 and x2 != 0) or y == 0 :
        print("闰年")
    else :
        print("不是闰年")
    """


   
    if (x1 == 0 and x2 != 0) or y == 0 :
        s = "是"
    else:
        s = "不是"
    print("{0}年{1}闰年".format(n, s))    #格式化字符串，n替换{0}，s替换{1}
    
