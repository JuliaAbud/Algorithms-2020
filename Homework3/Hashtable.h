#ifndef HASHTABLE_FILE
#define HASHTABLE_FILE

void initHash();
void intToBin(unsigned int n);
void createHMatrix(unsigned int n[]);
void printMatrix(unsigned int n[]);
int InsertKey(unsigned int x);
void printHashTable();
int SearchKey(unsigned int x);
int DeleteKey(unsigned int x);
unsigned int countSetBits(unsigned int n);

#endif