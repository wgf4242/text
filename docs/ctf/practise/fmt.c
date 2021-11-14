#include <stdio.h>
int main(){
        char a[100];
        scanf("%s",a);
        printf(a);
        return 0;
}
//gcc -m32 -pie -fno-stack-protector -o text fmt.c -Wno-format-security
//gcc -m32 -no-pie -fno-stack-protector -o text fmt.c -Wno-format-security
//泄露任意栈上的地址