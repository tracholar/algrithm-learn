#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define TREE_WIDTH 26
#define WORD_MAXLEN 256

struct trie_node {
	int count;	//the same word count
	int pass;	//subtree number.
	struct trie_node * next[TREE_WIDTH];
};

static struct trie_node root = {0,0,NULL};

int insert(const char * word){
	int i;
	struct trie_node *curr, *newnode;
	if(word[0] == 0){
		return 0;
	}

	curr = &root;
	for(i=0; ; i++){
		
		curr->pass++;
		if(word[i]==0)
			break;
		if(curr->next[ word[i]-'a' ] == NULL){
			newnode = (struct trie_node *)malloc(sizeof(struct trie_node));
			memset(newnode, 0, sizeof(struct trie_node));
			
			curr->next[ word[i]-'a' ] = newnode;
		}
		curr = curr->next[ word[i]-'a' ];
	}
	curr->count ++;
	return 0;

}

int search(struct trie_node * r, const char * word){

	if(r == NULL){
		return 0;
	}

	if(word[0]==0){
		return r->pass;
	}
	
	return search(r->next[ word[0]-'a' ], &word[1]);
}

int main(){
	int n, m, i,*ans;
	char word[WORD_MAXLEN + 1];
	scanf("%d", &n);
	for(i=0; i<n; i++){
		scanf("%s", word);
		insert(word);
	}

	scanf("%d", &m);
	ans = (int *)malloc(sizeof(int)*m);
	for(i=0; i<m; i++){
		scanf("%s", word);
		ans[i] = search(&root,word);
	}
	for(i=0;i<m;i++){
		printf("%d\n", ans[i]);
	}
	return 0;
}