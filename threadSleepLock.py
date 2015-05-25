#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print 'loop', nloop, ' start at:', ctime()
    print 'loop %d run for %d seconds' % (nloop, nsec)
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()

def main():
    print 'main thread start!'
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():pass

    print 'all done at:', ctime()

if __name__ == '__main__':
    main()
