//By : Julia Alejandra Rodríguez Abud
//Last modified: 12 September 2020

#include <stdio.h>
#include "clistint.h"

void clist_int(int arr[],size_t size){
    //%lu long unsigned int
    printf("Number of elements: %lu\n",size); 
    int i;
    for(i=0; i < size; i++){
        printf("%i ", arr[i]);
    }
    printf("\n");
}