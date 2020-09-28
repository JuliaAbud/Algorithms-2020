def bitOffset(int_type, offset):
    mask = 1 << offset #0100 & 0010 = 0000
    return(int((int_type & mask)/(pow(2,offset))))

def bitLen(n): 
    if (n == 0): 
        return 0   
    msb = 0 
    n = int(n / 2)   
    while (n > 0): 
        n = int(n / 2) 
        msb += 1   
    return (msb) 

def binaryCountingSort(A,offset):
    ceros = []
    unos = []    
    size = len(A)
    B = [ 0 for  i in range(0,size)]
    #print (C)
    
    for j in range(0,size):        
        if (bitOffset(A[j], offset)==0):
            ceros.append(A[j])            
        else:
            unos.append(A[j])            
    bCont=0
    for j in range(0,len(ceros)):
        B[bCont]= ceros[j]
        bCont = bCont +1
    for j in range(0,len(unos)):
        B[bCont]= unos[j]
        bCont = bCont +1
    return B

def binaryRadixSort(A):
    valorMaximo = max(A)
    for i in range(0,bitLen(valorMaximo)+1):
        A = binaryCountingSort(A,i)
    return (A)

if __name__ == "__main__":
    A = [10,989,9,667,6,52,5,13,1,61,7,6,10]

    print("Valor inicial")
    print(A)
    print("Valor Arreglado")
    A = binaryRadixSort(A)
    print(A)