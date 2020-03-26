"""
素数指的是只能被1和自身整除的正整数（不包括1）
"""
for ss in range (1, 101):
    if ss == 1:
        is_ss = False
    else :
        for i in range(2, ss):
            if ss % i == 0:
                is_ss = False
                break
            is_ss = True
        if is_ss == True:
            print(ss,end='  ')
    
