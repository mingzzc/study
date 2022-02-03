#include <stdio.h>

int main(int argc, const char * argv[]) {
    FILE *fd = fopen("file.txt", "r");
    char buf1[5];
    int result = fread(buf1, sizeof(char), 5, fd);
    printf("???%d %s?\n",result, buf1);
    return 0;
}
