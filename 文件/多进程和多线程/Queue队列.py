from multiprocessing import Queue, Process
import os
# 写入进程
def wp(q):
    print('进程%s开始写入:' % os.getpid())
    for i in range(100):
        q.put(i)
        print(i, end='\t')
    print()
    print('进程%s写入完成.' % os.getpid())
# 读取进程
def rp(q):
    print('进程%s开始读取' % os.getpid())
    while not q.empty():
        print(q.get(), end='\t')
    print()
    print('进程%s读取完成.' % os.getpid())

def main():
    q = Queue()
    p1 = Process(target=wp, args=(q,))
    p2 = Process(target=rp, args=(q,))
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()