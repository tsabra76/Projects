#Although Python's thread syntax is nicer than in many
#languages, it can still be a pain if all one wants to
# do is run a time-consuming function in a separate thread,
# while allowing the main thread to continue uninterrupted.
# A Future provides a legible and intuitive way to achieve
# such an end.

__author__ = 'Tarek'
from threading import *
import copy
import reprlib

class Future:

    def __init__(self,func,*param):
        # Constructor
        self.__done=0
        self.__result=None
        self.__status='working'

        self.__C=Condition()   # Notify on this Condition when result is ready

        # Run the actual function in a separate thread
        self.__T=Thread(target=self.Wrapper,args=(func,param))
        self.__T.setName("FutureThread")
        self.__T.start()

    def __repr__(self):
        return '<Future at '+hex(id(self))+':'+self.__status+'>'

    def __call__(self):
        self.__C.acquire()
        while self.__done==0:
            self.__C.wait()
        self.__C.release()
        # We deepcopy __result to prevent accidental tampering with it.
        a=copy.deepcopy(self.__result)
        return a

    def Wrapper(self, func, param):
        # Run the actual function, and let us housekeep around it
        self.__C.acquire()
        try:
            self.__result=func(*param)
        except:
            self.__result="Exception raised within Future"
        self.__done=1
        self.__status=repr(self.__result)
        self.__C.notify()
        self.__C.release()

