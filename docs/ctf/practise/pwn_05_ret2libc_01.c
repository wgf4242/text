#include <stdio.h>
#include<stdlib.h>
#include <unistd.h>

int main()
{
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    char addr[16];
    char buf[16];
    printf("You have one chance to read the memory!\n");
    printf("Give me the address in hex:");
    read(0, addr,0×10);
    unsigned long long iaddr=strtoll(addr,0,16);
    printf("\nContent: %lld\n", *(unsigned long long *)iaddr);
    printf("Give me your messege:");
    read(0, buf,0x90);
    return 0;
}