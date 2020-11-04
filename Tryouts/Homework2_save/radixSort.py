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
        self._rx.RadixSortBinary.argtypes = [self._singlepp, ctypes.c_int, ctypes.c_int] 
        self._rx.RadixSortBinary.restype = ctypes.c_void_p
        self._container = np.zeros(0, dtype = np.int32) 
        self._length  = ctypes.c_int(0) 

    def __del__(self):
        print('radixSort destroyed') 

    def RdxSort(self, maxLen):
        if type(self._container) is np.ndarray and len(self._container) > 0:
            if type(self._container[0]) is np.int32:
                #RadixSortBinary(int *arr, int n, int maxDigit);
                print("wtf")
                self._rx.RadixSortBinary(self._container,self._length,ctypes.c_int(maxLen))
            else:
                print('Error in the array dtype')
                sys.exit(-1)
        else:
            print('Error in the object not a ndarray or array null')
            sys.exit(-1)

    def read_data(self, arr):
        self._container = np.hstack([np.zeros(1, dtype = np.int32), arr]) 
        self._length  = ctypes.c_int(arr.shape[0])  

    def print_container(self):
        for i in range(1, len(self._container)):
            print(str(self._container[i]), end=' ')
        print('')