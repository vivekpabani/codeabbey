#include <stdio.h>

int main(void){

    int length, num, answer = 0, i;

    scanf("%d",&length);

    for(i=0; i<length; ++i){
        scanf("%d",&num);
        answer += num;
    }

    printf("%d", answer);
    return 0;
}
