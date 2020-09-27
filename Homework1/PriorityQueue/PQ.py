import sys
import os
import pathlib
import numpy as np
import ctypes
from numpy.ctypeslib import ndpointer 
sys.path.append(os.environ.get("AAVAR")+'/Heaps')
from heap import heap

class pQueue(heap):
    def __init__(self,htype="max"):
        super(pQueue, self).__init__(htype = 'max')
        # Load the shared library into c types.
        hPath = os.environ.get("AAVAR")+'/Heaps/cheap.so'
        sPath = os.environ.get("AAVAR")+'/PriorityQueue'
        ctypes.CDLL(hPath, mode=ctypes.RTLD_GLOBAL) 
        self._pq_name =  pathlib.Path(sPath).absolute() / "pQueue.so"
        self._singlepp = ndpointer(dtype = np.int32, ndim = 1, flags = 'C') 
        self._pq_name  = ctypes.CDLL(self._pq_name)
        # Set heap type
        self._theap = htype

        self._pq_name.insertMin.argtypes = [self._singlepp, ctypes.c_int, ctypes.c_int] 
        self._pq_name.insertMin.restype = ctypes.c_void_p 
        self._pq_name.insertMax.argtypes = [self._singlepp, ctypes.c_int, ctypes.c_int] 
        self._pq_name.insertMax.restype = ctypes.c_void_p 
        self._pq_name.extract.argtypes = [self._singlepp, ctypes.c_int] 
        self._pq_name.extract.restype = ctypes.c_int

    def __del__(self):
        print('PriorityQueue destroyed')

    def insertPQ(self,value):
        if type(self._container) is np.ndarray and len(self._container) > 0:
            # See if you have the correct dtype
            if type(self._container[0]) is np.int32:
                self._container = np.hstack([self._container, ctypes.c_int(0)]) 
                self._length = ctypes.c_int(self._container.shape[0])
                if self._theap == "max":
                    self._pq_name.insertMax(self._container, self._length, value)
                else:
                    self._pq_name.insertMin(self._container, self._length, value)
                #self.heapify(1)
                print("data insert: "+str(value))
            else:
                print('Error in the array dtype')
                sys.exit(-1)
        else:
            print('Error in the object not a ndarray or array null')
            sys.exit(-1)

    def extractPQ(self):
        if type(self._container) is np.ndarray and len(self._container) > 0:
            # See if you have the correct dtype
            if type(self._container[0]) is np.int32:
                self._length = ctypes.c_int(self._length.value-1) 
                v=self._pq_name.extract(self._container, self._length)
                self._container = np.split(self._container,[self._length.value, self._length.value+1]) [0]
                self.heapify(1)
                print("data extract: "+str(v))
            else:
                print('Error in the array dtype')
                sys.exit(-1)
        else:
            print('Error in the object not a ndarray or array null')
            sys.exit(-1)




            