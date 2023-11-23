// frida -l a02_breakpoint_addr.js -f crackme.exe

var addr = 0x0040155D
console.log(addr)
if (addr) {
        Interceptor.attach(ptr(addr), {
            onEnter: function (args) {
                let rax = this.context.rax;
                console.log('RAX value:', rax.toString(16));
                // assert(rax.toString(16) === '37387B4654435349')
            },
            onLeave(retval) {
                console.log('end');
            }
        }
    );
}
