'''
请输入一个整数：8
       ********
      *******
     ******
    *****
   ****
  ***
 **
*
'''
temp = input("请输入一个整数: ")
num = int(temp)
while num > 0 :
    print("+" * (num-1) + "*" * num)
    num = num - 1
    
