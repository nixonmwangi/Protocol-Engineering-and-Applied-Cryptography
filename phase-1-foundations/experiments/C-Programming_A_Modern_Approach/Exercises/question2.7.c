/* 
Write a program that asks the user to enter a U.S. dollar amount and then shows how to pay
that amount using the smallest number of $20, $10, $5, and $1 bills:
Enter a dollar amount: 93
$20 bills: 4
$10 bills: 1
$5 bills: 0
$1 bills: 3 
Hint: Divide the amount by 20 to determine the number of $20 bills needed, and then reduce
the amount by the total value of the $20 bills. Repeat for the other bill sizes. Be sure to use
integer values throughout, not floating-point numbers.
*/

#include <stdio.h>

int main (void){

    int amount, value, remain_value;
    int bill_20 = 20;
    int bill_10 = 10;
    int bill_5 = 5;
    int bill_1 = 1;

    // Enter amount

    printf("Enter dollar amount : ");
    scanf("%d", &amount);
    
    // 20 bills 

    value = amount/bill_20;
    printf("$20 bills : %d \n", value);

    remain_value = amount % bill_20;
    
    // 10 bills
    value = remain_value / bill_10;
    printf("$10 bills : %d \n", value);

    remain_value = remain_value % bill_10;
    
    // 5 bills
    value = remain_value / bill_5;
    printf("$5  bills : %d \n", value);

    // 1 bill
    value = remain_value % bill_5;
    printf("$1  bills : %d \n", value);


    return 0;
}