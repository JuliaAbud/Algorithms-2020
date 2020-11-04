#include <stdio.h>
#include <stdlib.h>
#include "queue.h"
#include "rxSort.h"

void RadixSortBinary(int *arr, int n, int maxDigit){ //PyObject *list , int
    printf("Entered the radix sort\n"); 
    int numBins =2;
    struct Queue* bins[numBins];
    for(int i=0;i<numBins;i++){
        bins[i]=createQueue(n);
    }
    printf("Created the bins\n"); 
    int maxDgt=maxDigit; 
    int currentDgt=0;
    int pow10 = 1;
    while(currentDgt<maxDgt){
        //We put the number in their respective bin (based on digit)
        for(int i=1; i<=n; i++){
            int digit = ((arr[i]/pow10)%10);
            enqueue(bins[digit],arr[i]);
        }
        printf("Finished putting them in buckets for this digit\n"); 
        //We take out elements of bins and put them in main array (First out)
        int mainArrayCounter=1;
        for(int j=0; j<numBins; j++){
                while(!isEmpty(bins[j])){
                arr[mainArrayCounter]=front(bins[j]);
                dequeue(bins[j]);
                mainArrayCounter++;
            }
        }
        printf("Finished putting them back for this digit\n"); 
        pow10 *=10;
        currentDgt++;
    }
}

