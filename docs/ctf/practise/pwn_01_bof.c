#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void you_c4n7_533_m3()
{
    execve("/bin/sh", (char *[]){0}, (char *[]){0});
}

int main(){
    char buf[16];
    puts("This is your first bof challenge ;)");
    fflush(stdout);
    read(0, buf, 0x30);
    return 0;
}