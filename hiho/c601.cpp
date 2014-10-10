#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define max(a,b) (a > b ? a : b)
/**
*	0,1±≥∞¸Œ Ã‚
*/
int N,M, *need, *value, *best;


int main(){
	int i, j, best1, best2;
	scanf("%d%d",&N, &M);
	need = (int *) malloc(sizeof(int) * N);
	value = (int *) malloc(sizeof(int) * N);
	best = (int *) malloc(sizeof(int) * M * N);
	for(i=0; i<N; i++){
		scanf("%d%d", need+i, value+i);
	}
	memset(best, 0, sizeof(int) * N * M);

	for(i=0; i<N; i++){
		for(j=0; j<M; j++){
			if((i-1)*M + j < 0) 
				best1 = 0;
			else
				best1 = best[(i-1)*M + j];
			if(j < need[i]){
				best2 = best[(i-1)*M + j];
			}
			else if((i-1)*M + j - need[i] < 0) 
				best2 = value[i];
			else
				best2 = best[(i-1)*M + j - need[i]] + value[i];
			
			best[i*M +j] = max(best1 , best2 );
		}
	}
	printf("%d\n",best[N*M-1]);
}