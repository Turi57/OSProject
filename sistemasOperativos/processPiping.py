#!/usr/bin/python
import os
import multiprocessing as mpr

#Custom class
class Message:
    def __init__(self,sender,text):
        self.sender = sender
        self.text = text

#Child's instructions to communicate with its parent
def child(pipeEnd):
    #Read parent's message
    message = pipeEnd.recv()
    print("Process {0}: Received \'{1}\' from process {2}".format(str(os.getpid()),message.text,str(message.sender)))
    
    #Send a message to the parent
    response = Message(os.getpid(), "Hello father")
    pipeEnd.send(response)


#Parent's instructions to communicate to the child
def parent(pipeEnd, childPID):
    #Send a message to the childProcess
    newMessage = Message(os.getpid(), "Hello child")
    pipeEnd.send(newMessage)
    
    #Read the message sent from the child process
    reply =  pipeEnd.recv()
    print("Process {0}: Received \'{1}\' from process {2}".format(str(os.getpid()),reply.text, str(reply.sender)))
    

####MAIN####

#Create pipe
(end1, end2) = mpr.Pipe()

#Fork process
newPID = os.fork()
if newPID == 0:
    child(end2)
else:
    parent(end1, newPID)
