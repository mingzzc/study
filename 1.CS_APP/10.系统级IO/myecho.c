#include <sys/types.h> 
#include <sys/stat.h> 
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

//打印默认缺省的envp就可以了
int main(int argc,char *argv[],char *envp[]) 
{
    //char s[100];
    //getenv(s);
    //printf("%s\n", getenv("PATH"));
    int i = 0;
    for (;;i++) {
        if (envp[i] == NULL) {
            break;
        }
        printf("env %d: %s\n", i, envp[i]);
    }
}