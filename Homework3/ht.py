import ctypes
import pathlib
import sys
import os

class hashTable():
    def __init__(self):
        def wrap_function(libr, funcname, restype, argtypes):
            func = libr.__getattr__(funcname)
            func.restype = restype
            func.argtypes = argtypes
            return func
        print("Initializing hashtable")
        sPath = os.environ.get("AAVAR")
        self._libname =  pathlib.Path(sPath).absolute() / "Hashtable.so"
        self._ht  = ctypes.CDLL(self._libname)
        #Funciones que nos traemos
        self._ht.initHash = wrap_function(self._ht, "initHash", None,  None)
        self._ht.printValues = wrap_function(self._ht, "printHashTable", None,  None)
        self._ht.insertKeyValue = wrap_function(self._ht, "InsertKey", ctypes.c_int, [ctypes.c_uint])
        self._ht.deleteKeyValue = wrap_function(self._ht, "DeleteKey", ctypes.c_int,  [ctypes.c_uint])
        self._ht.findKeyValue = wrap_function(self._ht, "SearchKey", ctypes.c_int, [ctypes.c_uint])
        #la inicializamos
        self._ht.initHash()

    def __del__(self):
        print('clear') 
    
    def insertKey(self, key):
        v = self._ht.insertKeyValue(ctypes.c_uint(key))
        print("Inserted key "+str(key)+" at index "+str(v))

    def deleteKey(self, key):
        v = self._ht.deleteKeyValue(ctypes.c_uint(key))
        print("Deleted key "+str(key)+" at index "+str(v))

    def findKey(self, key):
        v = self._ht.findKeyValue(ctypes.c_uint(key))
        print("Found key "+str(key)+" at index "+str(v))
    
    def printHashTable(self):
        self._ht.printValues()

    