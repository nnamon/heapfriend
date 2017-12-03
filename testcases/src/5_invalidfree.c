#include <stdlib.h>

int main() {
    int * a = (int *) malloc(sizeof(int));
    free(a+1);
}
