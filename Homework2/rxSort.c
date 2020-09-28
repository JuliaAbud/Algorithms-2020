#include <stdio.h>
#include <stdlib.h>
#include "queue.h"
#include "rxSort.h"

void RadixSortBinary(int *arr, int n, int maxDigit){
    int numBins =2;
    struct Queue* bins[numBins];
    for(int i=0;i<numBins;i++){
        bins[i]=createQueue(n);
    }
    int maxDgt= maxDigit; 
    for(int currentDgt=0, mask=1;currentDgt<maxDgt; currentDgt++, mask <<= 1){ 
        //We put the number in their respective bin (based on digit)
        printf("%d CurrentDigit \n", currentDgt); 
        for(int i=1; i<=n; i++){
            int digit = arr[i] & mask;
            digit = digit/pow(2,currentDgt);
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
    }
}

