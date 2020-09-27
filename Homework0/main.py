#Homework0: It sends a list from python to a reader in C
#Files clistint.c and clistint.h need to be compiled to libclistint.so

__author__ = "Julia Alejandra Rodríguez Abud"
__email__ = "Julia.Rodriguez@cinvestav.mx"
__date__= "12 September 2020"
__credits__ = ["Andres Mendez-Vazquez"]

import ctypes
import pathlib

#Finds the .so file needed
libname = pathlib.Path().absolute() / "libclistint.so"
c_lib = ctypes.CDLL(libname)

#Data to process
lista = [1, 2, 35, 4, 10, 357, -25, 16, 0]

#Create concrete array types by multiplying 
#any ctypes data type with a positive integer
arr = (ctypes.c_int * len(lista))(*lista)

#Sending the list and its size to C through the use of ctypes
c_lib.clist_int(arr,len(lista))

