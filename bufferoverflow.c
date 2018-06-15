#include <string.h>
#include <stdio.h>

void function2() {
printf("flow changed\n");
}

void function1(char *str){
char buffer[5];
strcpy(buffer, str);
}

int main(int argc, char *argv[])
{
function1(argv[1]);
printf("flow normal\n");
}
