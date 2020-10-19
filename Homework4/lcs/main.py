import os
import random
from timeit import timeit
import matplotlib.pyplot as plt

DNApossible = ['G','T','C','A']

def GenerateRandomSubsequence(P,n):
    R = []
    for x in range(n):
        R.append(random.choice(P))
    return R
def MutateSubsequence(A,P,per):
    for x in range(len(A)):
        r = random.random()
        if(r>=per):
            v = A[x]
            while (v==A[x]):
                A[x] = random.choice(P)
    return A

def LCSLength(X, Y): 
    m = len(X) 
    n = len(Y) 
    c = [[0]*(n+1)for i in range(m+1)] 
    b = [[None]*(n+1) for i in range(m+1)] 
    for i in range(1,m+1): 
        c[i][0] = 0
    for j in range(n+1): 
        c[0][j] = 0
    for i in range(1,m+1): 
        for j in range(1,n+1): 
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 'd' #diagonal 
            elif c[i-1][j]>=c[i][j-1]: 
                c[i][j]=max(c[i-1][j], c[i][j-1])
                b[i][j] = 'u' #up
            else: #if c[i-1][j]==c[i][j-1]
                c[i][j]=max(c[i-1][j], c[i][j-1])
                b[i][j] = 'l' #left
    print (c[m][n])
    return c,b

def printLCS(b,X,i,j):
    if(i==0 or j==0):
        return None
    if (b[i][j]=='d'):
        printLCS(b,X,i-1,j-1)
        print(X[i-1], end =" ")
    elif (b[i][j]=='u'):
        printLCS(b,X,i-1,j)
    else:
        printLCS(b,X,i,j-1)

def LCS(X,Y):
    #print (X)
    #print (Y)
    a = LCSLength(X,Y)
    printLCS(a[1],X,len(X),len(Y))
    print()
    
def showGraph(results1, results2, n, thispath):
    fig, ax = plt.subplots()
    ax.plot(n, results1,'blue',label='mutated by 20%')
    ax.plot(n, results2,'orange',label='mutated by 80%')

    ax.set(xlabel='input (n)', ylabel='time(s)', title='LCS of mutated DNA')
    ax.grid()
    ax.legend(loc='best', fancybox=True, shadow=True, ncol=1)

    fig.savefig(os.path.join(thispath, "lcs.png"))
    plt.show()


ta = []
tb = []
n = []
thispath = os.path.abspath(os.path.dirname(__file__))
for i in range(1,100):
    x = GenerateRandomSubsequence(DNApossible,i*5)
    y = MutateSubsequence(x,DNApossible,0.2)
    z = MutateSubsequence(x,DNApossible,0.8)
    t1 = timeit(stmt='LCS('+str(x)+','+str(y)+')', setup='from __main__ import LCS', number=1) 
    t2 = timeit(stmt='LCS('+str(x)+','+str(z)+')', setup='from __main__ import LCS', number=1) 
    ta.append(t1)
    tb.append(t2)
    n.append(i*5)
showGraph(ta,tb,n,thispath)

