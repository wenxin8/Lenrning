from multiprocessing import Queue, Process
def wp(q):
    for i in range(100):
        q.put(i)
        print(i, end='\t')
def main():
    q = Queue()
    p = Process(target=wp, args=(q,))
    p.start()
    p.join()
if __name__ == "__main__":
    main()   
