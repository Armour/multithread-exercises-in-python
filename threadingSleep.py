#coding: utf-8
import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print 'loop', nloop, 'start at:', ctime()
    print 'loop %d run for %d seconds' % (nloop, nsec)
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'main thread start!'
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = loop, args = (i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all donw at:', ctime()

if __name__ == '__main__':
    main()
