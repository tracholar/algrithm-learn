#include<stdio.h>
#include<stdlib.h>
#define HASHTABLE_SIZE 101
#define P 101

typedef struct {
	char * key;
	int val;
} hashNode, * HashTable;
int h1(const char * key){
	long long int phone;
	sscanf(key,"%lld",&phone);
	return (phone*P) % HASHTABLE_SIZE;
}
int h2(const char * key){
	long long int phone;
	sscanf(key,"%lld",&phone);
	return (phone*P) % (HASHTABLE_SIZE-1) + 1;
}
int hash(const char * key,int i){
	return (h1(key)+h2(key)*i) % HASHTABLE_SIZE;
}
void HashInsert(HashTable T,hashNode n){
	
}
int main(){
	
}