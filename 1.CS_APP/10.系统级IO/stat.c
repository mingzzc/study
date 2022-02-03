#include <sys/types.h> 
#include <sys/stat.h> 
#include <unistd.h>
#include <stdio.h>

int main()
{
    struct stat buf;
    stat("demo.txt", &buf);
    printf("%lld\n", buf.st_size);
    return 0;
}