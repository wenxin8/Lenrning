from multiprocessing import Process
from math import factorial
from time import time
class TaskProcess(Process):
    def __init__(seft, num):
        super().__init__()
        seft._num = num
    def run(self):
        start = time()
        factorial(self._num)
        end = time()
        print('耗时：%.5f秒' % (end-start))
def main():
    s = time()
    t1 = TaskProcess(1000000)
    t1.start()    
    t2 = TaskProcess(1000000)
    t2.start()
    t1.join()
    t2.join()
    e = time()
    print('总耗时：%.5f' % (e-s))
if __name__ == '__main__':
    main()        
