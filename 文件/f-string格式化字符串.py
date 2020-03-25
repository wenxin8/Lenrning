a = float(input("请输入a:"))
b = float(input("请输入b:"))
c = float(input("请输入c:"))
print("a+b+c="+ str(a + b +c))
print("a+b+c={}".format(a + b + c))
print("a+b+c=%s" % (a + b + c))

  # f-string
print(f"a+b+c={a + b + c}")
print(f"{a+b+c}")    #输出 6

  # 在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果：
print(f"{a+b+c=}")   #输出 1+2+3=6
