import numpy as np

#input sequence on numbers A, and value v
#output: index i such that v=A[i] or NIL if v does not appear in A
def search(array, v):
    i=-1
    for i in range(len(array)):
        if(array[i]== v):
            return i
            break
    return null

print(search([3,6,5,2],7))

