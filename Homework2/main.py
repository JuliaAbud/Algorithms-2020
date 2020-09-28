import numpy as np 
from radixSort import radixSort

if __name__ == "__main__":
    print("============")
    x = np.arange(100, 0, -1, dtype = np.int32 )
    print(x)
    HObject = radixSort()
    HObject.read_data(x)
    HObject.RdxSort()
    HObject.print_container()




    