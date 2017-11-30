#!/usr/bin/python

import os
import datetime

for i in range(2):
    print("Cycle: {0}".format(i))
    pid = os.fork()
    if pid == 0:
        print("{0} was created at {1}".format(os.getpid(),datetime.datetime.now()))
    else:
        print("{0} created {1}".format(os.getpid(),pid))



