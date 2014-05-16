#include<stdio.h>
#include<stdlib.h>

char* reverse_str(char* str){
	int i=0,j=0;
	char * strnew;
	while(str[i]!=0){
		i++;
	}
	strnew = (char*)malloc((i+1)*sizeof(*str));
	i--;
	for(j=0;i>=0;i--){
		strnew[j++] = str[i];
	}
	strnew[j] = 0;
	
	return strnew;
}
int main(int argc,char** argv){
	
	char * str = reverse_str(argv[1]);
	printf("%s\n",str);
	
}