import os
import ctypes
import numpy as np 
from numpy.ctypeslib import ndpointer 
import random
import matplotlib
import matplotlib.pyplot as plt
import time

def wrap_function(lib, funcname, restype, argtypes):
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

def FWtimer():   
    print("Floyd Warshall Algorithm Timer...")
    reps = 150 
    t = []  
    for x in range(2,reps+1):
        print("Iteracion con nxn : "+str(x))
        mtx = GenerateRandomMtxNil(30,-10,x)
        start = time.time()
        #row, col, mtx, print?
        Floyd_Warshall(x, x, mtx, 0) 
        t1 = time.time() - start
        t.append(t1)
    print("Sending to graph")
    showGraph(t, thispath)
    print("Complete*")

def showGraph(results1, thispath):
    fig, ax = plt.subplots()
    ax.plot(results1,'blue',label='FloydWarshall',linewidth=0.5)
    ax.set(xlabel='Matrix (nxn)', ylabel='time(s)', title='Floyd Warshall Algorithm')
    ax.legend(loc='best', fancybox=True, shadow=True, ncol=1)
    fig.savefig(os.path.join(thispath, "FloydWarshall_1.png"))
    plt.show()

def GenerateRandomMtxNil(size,valmin,valmax):
    mtx = np.random.randint(valmin, valmax + 1, size=(size,size))
    rows = mtx.shape[0]
    cols = mtx.shape[1]   
    for i in range(0, rows):
        for j in range(0, cols):
            if (random.uniform(0, 1)>0.6):
                mtx[i,j] = Nil
    return mtx

def ejercicio():
    print('_____________________________________')
    mtx = np.array([[0, 3, 8,Nil, -4],
                [Nil, 0, Nil, 1, 7],
                [Nil, 4, 0, Nil, Nil],
                [2, Nil, -5, 0, Nil],
                [Nil, Nil, Nil, 6, 0]], dtype=np.int32)
    Floyd_Warshall(5,5,mtx,1)
    print('_____________________________________')

if __name__=="__main__":
    thispath = os.path.abspath(os.path.dirname(__file__))
    libc = ctypes.CDLL(os.path.join(thispath, "FloydWarshall.so"))
    doublepp = ndpointer(dtype = np.int32, ndim=2, flags='C') 
    Floyd_Warshall = wrap_function(libc, "Floyd_Warshall", None, [ctypes.c_int, ctypes.c_int, doublepp, ctypes.c_int]) 
    Nil = 1000 
    ejercicio() 
    FWtimer()