#include <stdio.h>

int main(void){
    int n;
    int digits = 0;

    printf("Enter a non negative integer: ");
    scanf("%d", &n);
    
    do{
        n /= 10;
        digits++;
    }
    while ( n > 0);

    printf("The number has %d digits \n", digits);

    return 0;
}