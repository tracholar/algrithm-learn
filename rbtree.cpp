#include<stdio.h>
#include<stdlib.h>
#define R 0
#define B 1

typedef struct _rbnode{
	int key;
	bool color;
	struct _rbnode * lchild, * rchild;
	_rbnode(int k,bool c){
		key = k;
		color = c;
		lchild = NULL;
		rchild = NULL;
	}
} RBNode, * RBTree;

int main(){
	RBNode node(101,R);
	printf("%d\n",node.key);
}

