#include <stdio.h>
#include <stdbool.h>
int main(){
   int var1 = 1;
   float var2 = 1.0;
   bool var3 = true;
   bool var4 = false;
   char var5 = 'a';
   printf("%d\n",var1);
   printf("%f\n",var2);
   printf("%s\n", var3 ? "true" : "false");
   printf("%s\n", var4 ? "true" : "false");
   printf("%c\n",var5);
   
   return 0;
}