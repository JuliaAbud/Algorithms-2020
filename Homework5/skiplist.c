#include <stdlib.h>
#include <limits.h>
#include <stdio.h>
#include <time.h>
typedef struct node node;
#define PLUS_INF INT_MAX
#define MINUS_INF INT_MIN

typedef struct node {
    int value;
    node *up;
    node *down;
    node *right;
    node *left;
} node;

node *S_n;

int geth(node *n) {
    node *aux = n;
    int h = 0;
    while (aux->down != NULL){
        h++;
        aux=aux->down;
    }
    return h;
}

int flipCoins(node *n) {
    int result = 0;
    int h = geth(n);
    int i = 0;
    for (i = 0; i < h; i++)
    {
        result += rand() % 2;
    }
    return result;
}

node *crearNodo(int value) {
    node *n;
    n = (node *)malloc(sizeof(node));
    n->value = value;
    n->up = NULL;
    n->down = NULL;
    n->right = NULL;
    n->left = NULL;
    return n;
}

node *crearlista(int value) {
    node *ls = crearNodo(INT_MIN);
    node *le = crearNodo(INT_MAX);
    if (value == -1)
    {
        ls->right = le;
        le->left = ls;
    }
    else
    {
        node *n = crearNodo(value);
        ls->right = n;
        n->right = le;
        n->left = ls;
        le->left = n;
    }
    return ls;
}

void PrintSL(node *n) {
    node *aux = n;
    while (aux != NULL){
        node *aux2 = aux;
        while (aux2 != NULL)
        {
            {
                printf("\t%d", aux2->value);
            }
            aux2 = aux2->right;
        }
        aux = aux->down;
        printf("\n");
    }
}

void Insert(node *n, int value) {
    if (n == NULL)
        return;
    if (n->down == NULL){
        if (n->right->right == NULL){
           
            node * nuevalista = crearlista(value);
            n->right->down=nuevalista->right->right;
            n->down= nuevalista;
            nuevalista->up=n;
            nuevalista->right->right->up=n->right;
            return;
        }
        else{
            node *aux = n;
            node *nuevo = crearNodo(value);
            while (aux->value < value&&aux->right!=NULL){
                aux = aux->right;
            }
            nuevo->down = aux->down;
            nuevo->left = aux->left;
            nuevo->right = aux;
            aux->left->right = nuevo;
            aux->left = nuevo;
            int contador_caras = flipCoins(S_n);
            node *auxup = nuevo;
            int h = geth(S_n);
            if (contador_caras >= h){

                node *nivelnuevo = crearlista(-1);

                S_n->down->up = nivelnuevo;
                S_n->right->down->up = nivelnuevo->right;

                nivelnuevo->up = S_n;
                nivelnuevo->right->up = S_n->right;

                nivelnuevo->down = S_n->down;
                nivelnuevo->right->down = S_n->right->down;

                S_n->down = nivelnuevo;
                S_n->right->down = nivelnuevo->right;
            }
            int i;
            for (i = 0; i < contador_caras; i++){
                auxup->up = crearNodo(value);
                node *auxi = auxup->left;
                while (auxi->up == NULL)
                    auxi = auxi->left;
                auxi = auxi->up;
                auxup->up->down = auxup;

                auxup = auxup->up;

                node *auxd = auxi->right;
                auxup->left = auxi;
                auxup->right = auxd;

                auxd->left = auxup;
                auxi->right = auxup;
            }
        }
    }
    else{
        if (value > n->right->value)
            Insert(n->right, value);
        else
            Insert(n->down, value);
    }
}

int Delete(node *n, int value) {
    if (n == NULL)
        return 0;
    if (value == INT_MAX)
        return 0;
    node *aux = n;
    while (aux->value < value){
        aux = aux->right;
    }
    if (aux->value == value){
        while (aux!=NULL){
            node *aux2=aux;
            if(aux->right->value==INT_MAX&&aux->left->value==INT_MIN){
                aux->left->up->down=aux->left->down;
                aux->left->down->up= aux->left->up;
                free(aux->left);
                aux->right->up->down=aux->right->down;
                aux->right->down->up= aux->right->up;
                free(aux->right);
            }
            else{
            free(aux);
            aux2->left->right=aux2->right;
            aux2->right->left=aux2->left;
            }
            aux=aux2->down;
        }
        return 1;
    }
    else{
        if (aux->value < value){
            Delete(n->right, value);
        }
        else{
            Delete(n->down, value);
        }
    }
    return 0;
}

void wrapPrint() {
    PrintSL(S_n);
}
void wrapInsert(int value) {
    Insert(S_n, value);
}
int wrapDelete(int value) {
    return Delete(S_n, value);
}
void init() {
    srand(time(NULL));
    S_n = crearlista(-1);
    PrintSL(S_n);
}

/*
int main() {
    init();
    return 0;
}
*/