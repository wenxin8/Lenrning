from multiprocessing import Process
from time import time
def jc(num):    
    s = 1
    for i in range(1, num + 1):
        s = s * i
    return s    
def main():
    t1 = time()
    a = jc(111111)
    b = jc(111111)
    t2 = time()
    print('普通：%.5f' % (t2 - t1))
    t3 = time()
    p1 = Process(target=jc, args=(111111,))
    p1.start()
    p2 = Process(target=jc, args=(111111,))
    p2.start()
    p1.join()
    p2.join()
    t4 = time()
    print('多进程:%.5f' % (t4-t3))
if __name__ =='__main__':
    main()
