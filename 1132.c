#include <stdio.h>
#include <stdlib.h>
int main(){
  long long int x, y, i, n, v;
  v = 0;
  scanf("%lld %lld", &x, &y);
  if (x<y){
    for(i = x; i <= y; i++){
      if (i%13 != 0){
        v += i;
      }
    }
  }
  else if (y<x){
    for(i = y; i <= x; i++){
      if (i%13 != 0){
        v +=i;
      }
    }
  }
  printf("%lld\n", v);

  return(0);
}