#include <stdio.h>
#include <stdbool.h>
#include <math.h>
int main(){
   int a = 0;
   int b = 1;
   int entrada;
   int aux = 0;
   int i = 0;
   printf("Entar com o numero de fibonacci desejado: \n");
   scanf("%d", &entrada);
   printf("%d\n",a);
   printf("%d\n",b);
   while(i < (entrada - 2)){
   i = i + 1;
   aux = a + b;
   a = b;
   b = aux;
   printf("%d\n",b);
    
   };
   
   return 0;
}