#include<stdio.h>
#include<memory.h>
const int MAX = 1e+6 +1;
int d1[MAX];
int d2[MAX];
int main(){
    int T, M, N;
    scanf("%d",&T);
    for(int k = 0; k < T; ++k){
        memset(d1, 0, sizeof(d1));
        memset(d2, 0, sizeof(d2));
        int v1, v2;
        scanf("%d", &N);
        for(int i = 1; i < N; ++i){
            scanf("%d%d", &v1, &v2);
            ++d1[v1]; ++d1[v2];
        }
        scanf("%d", &M);
        for(int i = 1; i < M; ++i){
            scanf("%d%d", &v1, &v2);
            ++d2[v1]; ++d2[v2];
        }
        int D = 0, Mleaf = 0;
        for(int i = 1; i <= N; ++i){
            if(d1[i] > D) D = d1[i];
            if(d2[i] == 1) ++Mleaf;
        }
        if(M < 3) --Mleaf; // remove root Node 
        if(Mleaf == M - 1 && Mleaf <= (D + 1) / 2)
            printf("Case %d: NO\n", k+1);
        else printf("Case %d: YES\n", k+1);
    }
    return 0;
}