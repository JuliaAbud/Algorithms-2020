import ctypes
import pathlib
    
libname = pathlib.Path().absolute() / "Homework0/libclistint.so"
print(libname)
c_lib = ctypes.CDLL(libname)

lista = [1, 2, 35, 4, 10, 357, -25, 16, 0]
#Create concrete array types by multiplying any ctypes data type with a positive integer
#ctypes.Array(*args)     
arr = (ctypes.c_int * len(lista))(*lista)
c_lib.clist_int(arr,len(lista))