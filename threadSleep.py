#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import thread
from time import sleep, ctime

def loop0():
    print 'loop0 start at:', ctime()
    print 'loop0 for 4 seconds'
    sleep(4)
    print 'loop0 done at:', ctime()

def loop1():
    print 'loop1 start at:', ctime()
    print 'loop1 for 2 seconds'
    sleep(2)
    print 'loop1 done at:', ctime()

def main():
    print 'main thread start!'
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all done at:', ctime()

if __name__ == '__main__':
    main()
