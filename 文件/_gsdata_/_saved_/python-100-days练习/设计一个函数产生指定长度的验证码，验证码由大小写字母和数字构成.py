  #设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
import random
def generate_code(code_len = 4):
    all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

go_on = True
while go_on == True:
    
    print(generate_code(4))
    while True:
        yn = input("继续生成按y,退出按n:")
        if yn == 'y' or yn == 'Y' or yn == 'n' or yn == 'N':
            break
    if yn == 'n' or yn == 'N':        
        go_on = False
    
        
    
