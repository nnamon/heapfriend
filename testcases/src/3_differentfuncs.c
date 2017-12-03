#include <stdlib.h>

int main() {
    char * a, *b;

    a = (char *) malloc(0x100);
    b = (char *) calloc(0, 0x100);
    a = realloc(a, 0x200);
    free(a);
    free(b);
}
