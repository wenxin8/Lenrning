def mian_1()
    n, m = map(int, input().split())
    num1 = 0  # 正方形个数
    num2 = 0  # 长方形个数
    for i in range(0, n):
        for j in range(0, m):
            if i == j: # 横竖边长为1的边个数有(n-0)个(m-0)个，正方形个数为(n-0)(m-0)
                       # 横竖边长为2的边个数有 n-1个m-1个,所有正方形个数(n-1)*(m-1)
                num1 += (n - i) * (m - j)
            else:
                num2 += (n - i) * (m - j)
    print(num1, num2)

# n*m个方格，横向竖向的点数为n+1 和m+1,
#横竖各选两点组成矩形，
#所有矩形个数为 C(n+1,2)*C(m+1,2) = ((n+1)*n / 2！) * ((m+1)*m / 2！)
#A(m,n) = n!/(m-n)!
#C(m,n) = A(m,n)/n!= n!/((m-n)! * n!)
main_2():