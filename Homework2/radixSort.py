import sys
import os
import pathlib
import numpy as np
import ctypes
from numpy.ctypeslib import ndpointer 

class radixSort():
    def __init__(self):
        print("Initializing radixSort")
        sPath = os.environ.get("AAVAR")#+'/' 
        self._rx_name =  pathlib.Path(sPath).absolute() / "rxSort.so"
        self._singlepp = ndpointer(dtype = np.int32, ndim = 1, flags = 'C')
        self._rx  = ctypes.CDLL(self._rx_name)
        self._rx.RadixSortBinary.argtypes = [self._singlepp , ctypes.c_int, ctypes.c_int] 
        self._rx.RadixSortBinary.restype = ctypes.c_void_p
        self._container = [] 
        self._length  = 0
        self._maxLength = 0

    def __del__(self):
        print('radixSort destroyed') 

    def RdxSort(self):
        if len(self._container) > 0: 
            self._rx.RadixSortBinary(self._container,self._length,ctypes.c_int(self._maxLength))
        else:
            print('Error in the object array null')
            sys.exit(-1)

    def read_data(self, arr):
        self._container = np.hstack([np.zeros(1, dtype = np.int32), arr]) 
        self._length  = ctypes.c_int(arr.shape[0])  
        self.maxBinaryLen()
    
    def maxBinaryLen(self):
        n = max(self._container)
        if (n == 0): 
            return 0   
        maxL = 0 
        n = int(n / 2)   
        while (n > 0): 
            n = int(n / 2) 
            maxL += 1   
        maxL +=1
        self._maxLength = maxL

    def print_container(self):
        for i in range(1, len(self._container)):
            print(str(self._container[i]), end=' ')
        print('')