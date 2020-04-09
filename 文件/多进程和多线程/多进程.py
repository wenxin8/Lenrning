from multiprocessing import Process, Queue
from time import time


def f1():
    s = 0
    for i in range(0, 100000000):
        s += i
def f2():
    global result_queue
    s2 = 0
    for i in range(0, 50000000):
        s2 += i
    result_queue.put(s2)

def f3():
    global result_queue
    s3 = 0
    for i in range(50000000, 100000000):
        s3 += i
    result_queue.put(s3)
def main():
    result_queue = Queue()
    t1 = time()
    f1()
    t2 = time()
    # 多进程
    p1 = Process()
    p2 = Process()
    p1.run = f2
    p2.run = f3
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()

    t3 = time()
    print('单进程耗时：%.5f秒' % (t2 - t1))
    print('多进程耗时：%.5f秒' % (t3 - t2))

if __name__ == '__main__':
    main()

