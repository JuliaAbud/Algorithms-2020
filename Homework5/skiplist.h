#ifndef SKIPLIST_FILE
#define SKIPLIST_FILE

    typedef struct node node;
    int geth(node *n);
    int flipCoins(node *n);
    node *crearNodo(int value);
    node *crearlista(int value);
    void PrintSL(node *n);
    void wrapPrint());
    void Insert(node *n, int value);
    void wrapInsert(int value);
    int Delete(node *n, int value);
    int wrapDelete(int value);
    void init();
#endif
