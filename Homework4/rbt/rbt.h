#ifndef REDBLACK_FILE
#define REDBLACK_FILE

    typedef struct Node Node;
    typedef struct Tree Tree;
    void printNode(char* msg, Node *x);
    void leftRotate(Tree *T, Node *x);
    void rightRotate(Tree *T, Node *x);
    void insertFixup(Tree *T, Node *z);
    void insert(Tree *T, Node *z);
    void heightOfTree();
    Node* search(Node *N, int k);
    void insertInt(int i);
    int searchInt(int k);

#endif
