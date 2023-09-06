# printf to write
# Patch防御技巧
gcc -nostdlib -nodefaultlibs -fPIC -Wl,-shared hook.c -o hook
gcc vulner.c -o vulner