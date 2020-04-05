"""""
# r    只读文件。
# rb 二进制读文件。
# r+ 可读可写，不会创建不存在的文件 从头部开始写，会覆盖之前此位置的内容 。
# rb+ 二进制格式读写文件。文件指针将会放在文件的开头。
# w    只写文件，如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb 二进制写文件。
# w+ 读写文件。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+ 二进制读写文件。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a    只追写文件。从文件底部添加内容 不存在则创建 。
# ab 二进制追写文件。 从文件顶部读取内容 从文件底部添加内容 不存在则创建。
# a+ 追读写文件。从文件顶部读取内容 从文件底部添加内容 不存在则创建。
# ab+ 追读写二进制。从文件顶部读取内容 从文件底部添加内容 不存在则创建。
"""""
def main0():
    with open(file='test.txt', mode='r', encoding='utf-8') as f:
        print('访问模式：', f.mode)
        print('读取文件名：', f.name)
        f.seek(0, 0)  #seek(0)
        print('当前文件位置', f.tell())
        print('读取所有文件内容：\n',f.read())
        # readlines()按行读取所有内容，返回list
        print('当前文件位置：', f.tell())
        print('是否已关闭：', f.closed)
        # 不用with要用f.close()
    print('是否已关闭：', f.closed)

import time
def main1():
    f = None
    try:
        f = open('test.txt', 'r', encoding='utf-8')
        print(f.read())
        # 调用read()将读取整个文件，并将读取的游标留在文件的末尾
        # seek(0)将读取的光标返回到文件的开头
        f.seek(0)
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()
def main2():
    try:
        with open('test.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件！")
    except LookupError:
        print("指定了未知的编码！")
    except UnicodeDecodeError:
        print("读取文件是解码错误！")
def main3():# 逐行读取
    with open('test.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.2)
def main4():# 读取文件按行读取到列表中
    with open('test.txt', mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)
##################################################################
##################################################################
##################################################################
####写文件####
from math import sqrt
def is_prime(n):
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False
def main5():
    filename = ("素数.doc")
    i = 1
    try:
        f= open(filename, 'w', encoding= 'utf-8')
        f.write('0到10000之间的素数：\n')
        for number in range(1, 10000):
            if i == 16:
                i = 1
                f.write('\n')
            if is_prime(number):
                f.write(str(number) + '\t')
                i += 1
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        f.close()
    print('操作完成！')
