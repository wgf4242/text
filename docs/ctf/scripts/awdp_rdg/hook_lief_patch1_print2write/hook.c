// patch防御技巧
void myprintf(char *a,int b){
    //AT&T汇编格式
	asm(
		"mov %rdi,%rsi\n"
		"mov $0,%rdi\n"
		"mov $0x20,%rdx\n"
		"mov $0x1,%rax\n"
		"syscall\n"
		);
}
//gcc -nostdlib -nodefaultlibs -fPIC -Wl,-shared hook.c -o hook

// Intel汇编格式
// void myprintf(char *a,int b){
// 	asm(
// 		"mov rsi, rdi;\n"
// 		"mov rdi, 0;\n"
// 		"mov rdx, 0x20;\n"
// 		"mov rax, 0x1;\n"
// 		"syscall;\n"
// 		);
// }
// gcc -nostdlib -nodefaultlibs -fPIC -Wl,-shared hook.c -o hook
