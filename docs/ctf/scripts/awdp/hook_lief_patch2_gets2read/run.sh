# gets to write
# Patch防御技巧
gcc -Os -nostdlib -nodefaultlibs -fPIC -Wl,-shared hook_gets.c -o hook_gets
