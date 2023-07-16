#include <stdio.h>
#include <stdlib.h>
int main(int argc, char** argv) {
  printf("/bin/sh%d",102);
  puts("let's go\n");
  printf("/bin/sh%d",102);
  puts("let's gogo\n");
  return EXIT_SUCCESS;
}

// gcc vulner.c -o vulner