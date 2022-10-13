#include <stdio.h>

int main() {
  int I, G, J, E, SN, Iv, Gv;
  Iv = 0;
  Gv = 0;
  scanf("%d %d", &I, &G);
  E=0;
  J=1;
  if (I > G) {
    Iv++;
  }else if (G > I) {
    Gv++;
  }
  if (I == G) {
    E++;
  }
  printf("Novo grenal (1-sim 2-nao)\n");
  while(1) {
    scanf("%d", &SN);
    if (SN == 1) {
      J++;
      scanf("%d %d", &I, &G);
      if (I > G) {
      Iv++;
      } else if (G > I) {
      Gv++;
      } else{
      E++;
      }
      printf("Novo grenal (1-sim 2-nao)\n");
    } else if (SN == 2){
      break;
    }
  }

  printf("%d grenais\n", J);
  printf("Inter:%d\n", Iv);
  printf("Gremio:%d\n", Gv);
  printf("Empates:%d\n", E);
  if (Iv > Gv){
    printf("Inter venceu mais\n");
  } else if(Iv < Gv) {
    printf("Gremio venceu mais\n");
  } else if(Iv == Gv){
    printf("Nao houve vencedor\n");
  }
  return 0;
}
