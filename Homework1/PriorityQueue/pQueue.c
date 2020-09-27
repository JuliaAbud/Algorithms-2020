#include <stdio.h>
#include <stdlib.h>
#include "pQueue.h"
#include "../Heaps/cheap.h"

//the resize is being done from the py file

int extract( int *arr, int n){
  //remove the value in first position 
  int first = arr[1];
  arr[1] = arr[n];
  return first;
  //the array will be shrink after this point
}

void insertMin( int *arr, int n, int key){ 
    //inserts any int value in the last position of the array
    //the array has already grown by this point
    arr[n-1]= key; //we locate the new value at the end
    int current=n-1;
    int parent;
    while (current>1){
      parent=(current/2);
      if(arr[parent]>arr[current]){
          //switch with parent
          arr[parent]=arr[parent]^arr[current];
          arr[current]=arr[parent]^arr[current];
          arr[parent]=arr[parent]^arr[current];
          current=parent;
      }else{
        break;
      }

    }
}

void insertMax( int *arr, int n, int key){ 
    //inserts any int value in the last position of the array
    //the array has already grown by this point
    arr[n-1]= key; //we locate the new value at the end
    int current=n-1;
    int parent;
    while (current>1){
      parent=(current/2);
      if(arr[parent]<arr[current]){
          //switch with parent
          arr[parent]=arr[parent]^arr[current];
          arr[current]=arr[parent]^arr[current];
          arr[parent]=arr[parent]^arr[current];
          current=parent;
      }else{
        break;
      }

    }
}


