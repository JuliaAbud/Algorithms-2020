#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "FloydWarshall.h"
#define nil 1000

void printArray(int cols, int rows, int (*arr)[cols] ){ 
    int row, columns;
    for (row=0; row<rows; row++)
    {
        for(columns=0; columns<cols; columns++)
        {
            if(arr[row][columns]!=1000)
                printf("%d     ", arr[row][columns]);
            else
                printf("nil     ");
        }
        printf("\n");
    } 
    printf("==============================\n");
} 
void Floyd_Warshall(int rows, int cols, int (*W)[cols], int printData){
    int n = rows;
    int i, j, k; 
    int D[rows][cols]; 
    int Pi[rows][cols]; 
    int Dnext[rows][cols]; 
    int Pinext[rows][cols]; 
    memcpy(D, W, cols * rows * sizeof(int));
    memset(Pi, -1, cols * rows * sizeof(int));

    for (i = 0; i < rows; i++){ 
      for (j = 0; j < cols; j++){
        if (D[i][j] < nil){
            Pi[i][j] = i + 1;
        }
      }
    }

    for (k = 0; k < n; k++){ 
        memset(Dnext, 0, cols * rows * sizeof(int));
        memset(Pinext, -1, cols * rows * sizeof(int));
        for (i = 0; i < rows; i++){ 
            for (j = 0; j < cols; j++){
                if (D[i][j] > D[i][k]+D[k][j]){
                    Dnext[i][j] = D[i][k]+D[k][j];
                    Pinext[i][j] = Pi[k][j];
                }
                else{
                    Dnext[i][j] = D[i][j];
                    Pinext[i][j] = Pi[i][j];
                }
            }
        }
        for (i = 0; i < rows; i++){ 
            for (j = 0; j < cols; j++){
                D[i][j] = Dnext[i][j];
                Pi[i][j] = Pinext[i][j];
            }
        }
        if(printData!=0){
            printf("D%d\n-----------\n",k);
            printArray(rows, cols, D);
            printf("Pi%d\n-----------\n",k);
            printArray(rows, cols, Pi);
        }
    }
    printf("FINISHED\n");
}

int ejemplo(){
    printf("Start Code\n");
    int W[5][5]= {
            {0, 3, 8, nil, -4},
            {nil, 0, nil, 1, 7},
            {nil, 4, 0, nil, nil},
            {2, nil, -5, 0, nil},
            {nil, nil, nil, 6, 0}
                };
    printArray(5, 5, W);
    Floyd_Warshall(5, 5, W, 1); 
    return -1;
}
int main(){
    ejemplo();
    return -1;
}