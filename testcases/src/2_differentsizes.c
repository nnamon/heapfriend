#include <stdlib.h>

int main() {
    void * a, * b, * c, * d, * e, * f;
    a = (char *) malloc(0x10);
    b = (char *) malloc(0x100);
    c = (char *) malloc(0x1000);
    d = (char *) malloc(0x10000);
    e = (char *) malloc(0x100000);
    f = (char *) malloc(0x100000);

    free(a);
    free(b);
    free(c);
    free(d);
    free(e);
    free(f);
}
