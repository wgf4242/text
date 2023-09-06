// patch防御技巧
void mygets(char *a,int b){
	// 32bits int 0x80;   64bits syscall;
	asm(
		"mov $0x3,%eax\n"
		"mov $0, %ebx\n"
		"mov %eax, %ecx\n"
		"mov $0x20,%edx\n"
		"int $0x80\n" 
		"nop\n"
		"nop\n"
		"nop\n"
		"nop\n"
		"nop\n"
		);
}
//gcc -Os -nostdlib -nodefaultlibs -fPIC -Wl,-shared hook_gets.c -o hook_gets


// 64bits
// void mygets(char *a,int b){
// 	// 32bits int 0x80;   64bits syscall;
// 	asm(
// 		"mov $0x0,%rax\n"
// 		"mov %rdi, %rsi\n"
// 		"mov $0, %rdi\n"
// 		"mov $0x20,%rdx\n"
// 		"syscall\n" 
// 		"nop\n"
// 		"nop\n"
// 		"nop\n"
// 		"nop\n"
// 		"nop\n"
		
// 		);
// }