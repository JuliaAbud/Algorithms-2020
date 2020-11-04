import os
import ctypes
import matplotlib
import matplotlib.pyplot as plt
from math import log2
from timeit import timeit
from random import randint, randrange, shuffle

def wrap_function(lib, funcname, restype, argtypes):
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func


def SLtimer():

    thispath = os.path.abspath(os.path.dirname(__file__))
    libc = ctypes.CDLL(os.path.join(thispath, "skiplist.so"))

    global SL_init
    global SL_insert
    global SL_delete
    global SL_print
    SL_init   = wrap_function(libc, "init", None, None)
    SL_insert = wrap_function(libc, "wrapInsert", None, [ctypes.c_int])
    SL_delete = wrap_function(libc, "wrapDelete", ctypes.c_int, [ctypes.c_int])
    SL_print  = wrap_function(libc, "wrapPrint", None, None)
    
    print("Init skipList..")
    SL_init()
    print("Insertions...")
    reps = 1000 
    i = [] #insert's times
    d = [] #delete's times
    l = [] #log(n) values

    randominputs = set()
    while len(randominputs)<reps:
        randominputs.add(randint(0, reps))
    randomlist = list(randominputs)
    shuffle(randomlist)

    SL_insert(reps+1)
    j = 0
    for x in randomlist:
        t1 = timeit(stmt='SL_insert('+str(x)+')', setup='from __main__ import SL_insert', number=1) 
        t3 = log2(j+1)/30000 
        i.append(t1)
        l.append(t3)
        j+=1
    
    #SL_print()
    j = 0
    for x in randomlist:
        t2 = timeit(stmt='SL_delete('+str(x)+')', setup='from __main__ import SL_delete', number=1) 
        d.append(t2)
        j+=1
    list.reverse(d)

    print("Sending to graph")
    showGraph(i, d, l, thispath)
    print("Complete")


def showGraph(results1, results2, results3, thispath):
    fig, ax = plt.subplots()
    ax.plot(results3,'black',label='log n',linewidth=0.5)
    ax.plot(results2,'red',label='delete',linewidth=0.5)
    ax.plot(results1,'blue',label='insert',linewidth=0.5)

    ax.set(xlabel='input (n)', ylabel='time(s)', title='Skiplist')
    ax.legend(loc='best', fancybox=True, shadow=True, ncol=1)

    fig.savefig(os.path.join(thispath, "skiplist_1.png"))
    plt.show()

if __name__=="__main__":
    SLtimer()
