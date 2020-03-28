  # 设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(x):
    if x[0] > x[1]:
        m1, m2 = x[0], x[1]
    elif x[0] < x[1]:
        m1, m2 = x[1], x[0]
    for index in range(1,len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

a = [1, 4, 3, 2, 6, 9, 8, 7, 5]
print(max2(a))
x, y = max2(a)
print(x, y)
    
        
    