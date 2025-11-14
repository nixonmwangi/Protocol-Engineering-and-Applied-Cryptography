/*
Write a program that formats product information entered by the user. A session with the
program should look like this:
Enter item number: 583
Enter unit price: 13.5
Enter purchase date (mm/dd/yyyy): 10/24/2010
Item
583
Unit
Price
$ 13.50
Purchase
Date
10/24/2010
*/
#include <stdio.h>
int main(void)
{
int item;
float price;
int day, month, year;

printf("Enter item number : ");
scanf("%d", &item);
printf("Enter unit price  : ");
scanf("%f", &price);
printf("Enter purchase date (mm/dd/yyyy) : ");
scanf("%d/%d/%d", &day, &month, &year);
printf("Item\t Unit\t Purchase Date\n");
printf("%d\t %.2f\t %d/%d/%d\n",item, price, day, month, year);
return 0;
}