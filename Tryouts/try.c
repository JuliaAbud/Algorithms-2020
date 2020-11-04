#include <stdio.h>
/*Funcion main*/
int main()
{
    printf("Hola ---------------------------------------------------------------------\n");
    int num1;
    int num2;
    int resultado;
    printf("ingrese priemr valor \n");
    scanf("%d",&num1); //%d entero decimal
    printf("ingrese segundo valor \n");
    scanf("%d",&num2); //%d entero decimal
    resultado=num1+num2;
    printf("Resultado: %d \n",resultado);
    return 0;
}

//gcc try.c -o try.o
//./try.out