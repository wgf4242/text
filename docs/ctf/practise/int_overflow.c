#include <limits.h>
#include <stdio.h>
int main(int argc, char const *argv[])
{
	int i;
	i = INT_MAX;// 2 147 483 647
	i++;
	printf("i = %d\n", i);// i = -2 147 483 648

	i = INT_MIN;// -2 147 483 648
	i--;
	printf("i = %d\n", i);// i = 2 147 483 647

	unsigned int ui;
	ui = UINT_MAX;// 在 x86-32 上为 4 294 967 295
	ui++;
	printf("ui = %u\n", ui);// ui = 0
	ui =0;
	ui--;
	printf("ui = %u\n", ui);// 在 x86-32 上，ui = 4 294 967 295


	int j;
	j = 2147483647;
	printf("j = %d\n", j>9);// i = -2 147 483 648
	printf("%d\n", 0xffffffff+1); // 0

	return 0;
}