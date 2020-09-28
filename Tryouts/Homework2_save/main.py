import numpy as np 
from radixSort import radixSort

def intArrayToBinary():
    print("array")
    

if __name__ == "__main__":
    print("============")
    x = np.arange(100, 0, -1, dtype = np.int32 )
    #lis=np.array([1,2,3,4,5,6,7,8,9][np.array(1)])
    #print(lis)
    #x=np.binary_repr(lis,width=32)
    #binary_repr_vec = np.vectorize(np.binary_repr)
    #binary_repr_vec(lis, width=32)

    print(x)
    HObject = radixSort()
    HObject.read_data(x)
    HObject.RdxSort(6)
    HObject.print_container()



    