#!/usr/bin/python

import os

listPID = []
isParent = True

for i in range(10):
    if isParent:
        pid = os.fork()
 
        #If the process is the child process
        if pid == 0:
            isParent = False #Inhibit the child process of forking
        else:
            listPID.append(pid)

#Only print the list of PIDs created stored in the parent process 
if isParent:
    print(listPID)

