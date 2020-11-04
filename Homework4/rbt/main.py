import os
import ctypes
import matplotlib
import matplotlib.pyplot as plt
from math import log2
from timeit import timeit
from random import randint

def wrap_function(lib, funcname, restype, argtypes):
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

def rbtOperations():
    thispath = os.path.abspath(os.path.dirname(__file__))
    libc = ctypes.CDLL(os.path.join(thispath, "rbt.so")) 

    global rbtInsert 
    global rbtSearch 
    rbtInsert= wrap_function(libc, "insertInt", None, [ctypes.c_int])
    rbtSearch = wrap_function(libc, "searchInt", ctypes.c_int, [ctypes.c_int])

    print("Start insertion process...")

    i = []
    s = []
    l = []
    for x in range(1000):#5000
        r = randint(0, 10000)
        t1 = timeit(stmt='rbtInsert('+str(r)+')', setup='from __main__ import rbtInsert', number=1) 
        t2 = timeit(stmt='rbtSearch('+str(r)+')', setup='from __main__ import rbtSearch', number=1)
        t3 = log2(x+1)
        i.append(t1)
        s.append(t2)
        l.append(t3/60/1000)
    
    showGraph(i,s,l,thispath)
    print("Completed process")

def showGraph(results1, results2, results3, thispath):
    fig, ax = plt.subplots()
    ax.plot(results3,'black',label='log n')
    ax.plot(results2,'red',label='search')
    ax.plot(results1,'blue',label='insert')

    ax.set(xlabel='input (n)', ylabel='time(s)', title='RBT')
    ax.legend(loc='best', fancybox=True, shadow=True, ncol=1)

    fig.savefig(os.path.join(thispath, "rbt_1.png"))

    #ax.plot(results3,'gray',label='log(n)')
    #ax.plot(results1,'blue',label='insert')
    #ax.plot(results2,'orange',label='search')

    #ax.set(xlabel='input (n)', ylabel='time(s)', title='Red black tree')
    #ax.grid()
    #ax.legend(loc='best', fancybox=True, shadow=True, ncol=1)

    #fig.savefig(os.path.join(thispath, "rbt.png"))
    plt.show()


if __name__=="__main__":
    rbtOperations()

