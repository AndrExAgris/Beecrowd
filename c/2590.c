#include <stdio.h>

int main() {
  int x;
  scanf("%d", &x);
  
  int list[4];
  list[0] = 1;
  list[1] = 7;
  list[2] = 9;
  list[3] = 3;

  int i, n;
  for( i=0; i<x; i++) {
    scanf("%d", &n);
    n = n%4;

    if(n == 0){
      printf("1\n");
    }
    if(n == 1){
      printf("7\n");
    }
    if(n == 2){
      printf("9\n");
    }
    if(n == 3){
      printf("3\n");
    }
  }

  return 0;
}