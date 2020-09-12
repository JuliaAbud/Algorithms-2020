#include <stdio.h>
#include "clistint.h"

void clist_int(int arr[],size_t size){
    printf("Number of elements: %lu\n",size); //%lu long unsigned int
    int i;
    for(i=0; i < size; i++){
        printf("%i ", arr[i]);
    }
    printf("\n");
}