#include <stdio.h>
#include <stdbool.h>
#include <math.h>
int main(){
   int var1 = 2;
   int var2 = 3;
   int resultado1;
   resultado1 = var1 + var2;
   printf("%d\n",resultado1);
   resultado1 = var1 - var2;
   printf("%d\n",resultado1);
   resultado1 = var2 % var1;
   printf("%d\n",resultado1);
   float resultado2;
   resultado2 = var1 * var2;
   printf("%f\n",resultado2);
   resultado2 = var1 / var2;
   printf("%f\n",resultado2);
   resultado2 = pow(var1,var2);
   printf("%f\n",resultado2);
   
   return 0;
}