#include <stdio.h>

int main(void) {
    int a, b, c, d;
    int max1, min1, max2, min2;
    int largest, smallest;

    printf("Enter four integers: ");
    scanf("%d %d %d %d", &a, &b, &c, &d);

    // IF #1
    if (a > b) {
        max1 = a;
        min1 = b;
    } else {
        max1 = b;
        min1 = a;
    }

    // IF #2
    if (c > d) {
        max2 = c;
        min2 = d;
    } else {
        max2 = d;
        min2 = c;
    }

    // IF #3
    if (max1 > max2)
        largest = max1;
    else
        largest = max2;

    // IF #4
    if (min1 < min2)
        smallest = min1;
    else
        smallest = min2;

    printf("Largest: %d\n", largest);
    printf("Smallest: %d\n", smallest);

    return 0;
}
