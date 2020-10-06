#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
#include "Hashtable.h"

int h(unsigned int x);
unsigned int hMatrix[6];
unsigned int hTable[64];

void createHMatrix(unsigned int n[]){
    for (int i=0;i<64;i++)
        hTable[i]=-1;
    for (int i=0;i<6;i++)
        n[i]=rand();
}

void printMatrix(unsigned int n[]){
    printf("==========HASH TABLE===========\n");
    for (int i=0;i<6;i++)
        intToBin(n[i]);
    printf("================================\n\n");
}

void intToBin(unsigned int n){
    int c,k;    
    for (c = 31; c >= 0; c--)
        {
            k = n >> c;
            if (k & 1)
                printf("1");
            else
                printf("0");
        }
    printf("\n");
}

unsigned int countSetBits(unsigned int n) 
{ 
    unsigned int count = 0; 
    while (n) { 
        count += n & 1; 
        n >>= 1; 
    } 
    return count; 
} 

int h(unsigned int x){
    int valor=0;
    int binarios[]={1,2,4,8,16,32};
    for (int i=0;i<6;i++){
        valor += (countSetBits(hMatrix[i] & x) % 2)*binarios[i];
    }
    return valor;
}

int SearchKey(unsigned int x){
    if(x<4294967295 && x>=0){
        for(int i=0;i<64;i++){
            if (hTable[(h(x)+i)%64]==x){
                return (h(x)+i)%64;
            }else if(hTable[(h(x)+i)%64]==-1){
                return -1;
            }
        }
        return -1;            
    }        
    else{
        printf("Value out of range");
        return -1;
    }
}

int InsertKey(unsigned int x){
    if(x<4294967295 && x>=0){
        for(int i=0;i<64;i++){
            if (hTable[(h(x)+i)%64]==-1){
                hTable[(h(x)+i)%64]=x;
                return (h(x)+i)%64;
            }
        }
        printf("This hash table is full");
        return -1;            
    }        
    else{
        printf("Value out of range");
        return -1;
    }
}

void printHashTable(){
    for(int i=0;i<64;i++){
        if(i%8==0 && i>1)
            printf("\n");
        printf("idx= %d, key =%d | ", i, hTable[i]);    
    }
    printf("\n");
}

int DeleteKey(unsigned int x){
    if(x<4294967295 && x>=0){
        int index = SearchKey(x);
        if (index ==-1){
            printf("The key wasn't found");
            return -1;
        }            
        else{
            hTable[index]=-1;
            int point = index;
            for(int i=1;i<64;i++){                
                if (hTable[(point+i)%64]!=-1){
                    if((h(hTable[(point+i)%64])<(point+i)%64)&&(h(hTable[(point+i)%64])>=(index))){ 
                        hTable[point]=hTable[(point+i)%64];
                        point=(point+i)%64;
                        hTable[point]=-1;
                    }
                }else{ 
                    return index;
                }
            }
            return index;
        }      
     
    }else{
        printf("Value out of range");
        return -1;
    }
}


void initHash(){
    srand(time(NULL));
    createHMatrix(hMatrix);
    printMatrix(hMatrix); 
}
