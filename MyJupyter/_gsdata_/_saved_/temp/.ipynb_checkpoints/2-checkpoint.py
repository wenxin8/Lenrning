from multiprocessing import Process
from time import time
def jc(num):    
    s = 1
    for i in range(1, num + 1):
        s = s * i
    return s    
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
# print('多进程：%.5f' % (t4-t3))
# class Jctask(Process):
#     def __init__(self, num):
#         super().__init__()
#         self._num = num
#     def run(self):
#         s = 1
#         for i in range(1, self._num + 1):
#             s = s * i
#         return s
# start = time()
# t1 = Jctask(111111)
# t1.start()
# t2 = Jctask(111111)
# t2.start()
# t1.join()
# t2.join()
# end = time()
# print('类多进程：%.5f' % (end-start))
