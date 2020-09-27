import numpy as np 
from PQ import pQueue

if __name__ == "__main__":

    print("\n Data generated: ")
    x = np.arange(10, 0, -1, dtype = np.int32 )
    print(x)
    print("Build Heap Min: =====================")
    HObject = pQueue(htype="min")
    HObject.read_data(x)
    HObject.build_heap()
    HObject.print_container()
    print("Modify Min Heap: =======================")
    HObject.insertPQ(20)
    HObject.print_container()
    HObject.extractPQ()
    HObject.print_container()

    print("\n Data generated: ")
    y = np.arange(10, 20, 1, dtype = np.int32 )
    print(y)
    print("Build Heap Max: =======================")
    HObject2 = pQueue(htype="max")
    HObject2.read_data(y)
    HObject2.build_heap()
    HObject2.print_container()
    print("Modify Max Heap: =======================")
    HObject2.insertPQ(1)
    HObject2.print_container()
    HObject2.extractPQ()
    HObject2.print_container()