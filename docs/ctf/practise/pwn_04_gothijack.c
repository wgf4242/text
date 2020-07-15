#include <stdio.h>
#include <stdlib. h>
#include <unistd.h>

char name[64];

int main()
{
	int unsigned long long addr;
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	printf("What's you name?\n");
	read(o, name, 0x40);
	printf("Where do you want to write?\n");
	scanf("%llu", &addr);
	printf("Data: ");
	read(0,(char *)addr, 8);
	puts("Done!");
	printf("Thank you %s!\n", name);
	return 0;
}