#include <stdio.h>
#include <stdbool.h>
#include <math.h>
int main(){
   int aa = 5;
   int bb = 2;
   float pi = 3.1415;
   float res;
   res = aa + bb * pi;
   printf("%f\n",res);
   res = (aa + bb) * pi;
   printf("%f\n",res);
   res = bb * pi + aa;
   printf("%f\n",res);
   res = bb * (pi + aa);
   printf("%f\n",res);
   
   return 0;
}