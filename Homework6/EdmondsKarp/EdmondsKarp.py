#Edmonds-Karp Algorithm
import os
import random
import matplotlib
import matplotlib.pyplot as plt
import time

def EdmondsKarp(C, s, t):
        n = len(C) # C is the capacity matrix
        F = [[0] * n for i in range(n)]
        path = bfs(C, F, s, t)
        print('Path Found: '+str(path))
        while path != None:
            flow = min(C[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            #Blocks the paths that are adjacent to the vertices in the path
            for u,v in path:
                if u > 0:
                    for cols in range (1,n): 
                        if cols != v :
                            C[u][cols] = 0
                    for rows in range (1,n): # 
                        if rows != v :
                           C[rows][u] = 0              
            path = bfs(C, F, s, t)
            print('Path Found: '+str(path))
        return sum(F[s][i] for i in range(n))

def bfs(C, F, s, t):
        queue = [s]
        paths = {s:[]}
        if s == t:
            return paths[s]
        while queue: 
            u = queue.pop(0)
            for v in range(len(C)):
                    if(C[u][v]-F[u][v]>0) and v not in paths:
                        paths[v] = paths[u]+[(u,v)]
                        if v == t:
                            return paths[v]
                        queue.append(v)
        return None
    
def CreateCapacityGraph(M):
    rows = len(M)
    cols = len(M[0])
    vertices = (rows*cols)+2
    source=0
    sink=vertices-1
    startvertices=0
    capacity = [[0 for i in range(vertices)] for j in range(vertices)]
    for i in range(rows):
        for j in range(cols):
            n=(i*cols)+j+1
            #Connect the vertices in the borders to the Sink
            if i == 0 or j == 0 or i == cols-1 or j == rows-1: 
                capacity[n][sink]=1
            #Connects the Source to the vertices with a mark
            if M[i][j]==1: 
                startvertices += 1
                capacity[source][n]=1
            #Look for the 4 neighbors of this vertex (that are not startvertices)
            if(i>0 and M[i-1][j]!=1):
                up=((i-1)*cols)+j+1
                capacity[n][up]=1
            if(i<cols-1 and M[i+1][j]!=1):
                down=((i+1)*cols)+j+1
                capacity[n][down]=1
            if(j>0 and M[i][j-1]!=1):
                left=(i*cols)+j
                capacity[n][left]=1
            if(j<rows-1 and M[i][j+1]!=1):
                right=(i*cols)+j+2
                capacity[n][right]=1
    return capacity,startvertices

def GenerateBinaryMatrix(n):
    print('Generate Matrix of :'+str(n)+'x'+str(n))
    mtx = [[0 for i in range(n)] for j in range(n)]
    for x in range(n):
        for y in range(n):             
            if (random.uniform(0, 1)>.5):
                mtx[x][y] = 1
    return mtx

def PrintArray(A):
    for a in range(len(A)):
        print(A[a])

def showGraph(results1, results2, results3, thispath):
    fig, ax = plt.subplots()
    ax.plot(results2,'red',label='Generate Capacity Matrix',linewidth=0.5)
    ax.plot(results1,'blue',label='Edmonds-Karp',linewidth=0.5)
    ax.plot(results3,'orange',label='All process',linewidth=0.5)

    ax.set(xlabel='Escape matrix (nxn)', ylabel='time(s)', title='Escape Problem')
    ax.legend(loc='best', fancybox=True, shadow=True, ncol=1)

    fig.savefig(os.path.join(thispath, "escapeProblem_1.png"))
    #plt.show()

def Exercise26():
    # Escape Grid
    A = [[ 0, 0, 0, 0, 0, 0],  
        [ 0, 1, 0, 1, 0, 1],   
        [ 1, 1, 0, 1, 1, 1], 
        [ 0, 1, 0, 1, 0, 1], 
        [ 0, 0, 0, 0, 0, 0], 
        [ 0, 0, 0, 0, 0, 0] ]
    PrintArray(A)
    C = CreateCapacityGraph(A) 
    source = 0  
    sink = len(C[0])-1  
    max_flow = EdmondsKarp(C[0], source, sink)
    print ("Edmonds-Karp Algorithm")
    print ("Marked points: ", str(C[1]))
    print ("Maximum Flow: ", str(max_flow))
    if(max_flow==C[1]):
        print("Every mark was able to escape")
    else:
        print("Some marks were not able to escape")

def GraphTime():
    thispath = os.path.abspath(os.path.dirname(__file__))
    c = [] #Capacity Matrix times
    e = [] #Edmonds Karp times
    a = [] #All process times

    for x in range(15):
        B=GenerateBinaryMatrix(x+1)
        start = time.time()
        C = CreateCapacityGraph(B) 
        t1 = time.time() - start
        source = 0  
        sink = len(C[0])-1  
        start = time.time()
        EdmondsKarp(C[0], source, sink)
        t2 = time.time() - start
        c.append(t1)
        e.append(t2)
        a.append(t1+t2)

        showGraph(c, e, a, thispath)
        
if __name__=="__main__":
    #GraphTime()
    Exercise26()
