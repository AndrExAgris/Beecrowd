#include <stdio.h>

int main() {
  int x = 0, y = 0, i = 0, aux;
  scanf("%d %d", &x, &y);

  if(x>y){
    aux = x;
    x = y;
    y = aux;
  }
  for(i = x+1 ; i < y; i++){
    if(i%5 == 2 || i%5 == 3){
      printf("%d\n", i);
    }
  }
  return 0;
}