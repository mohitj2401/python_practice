#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, value, i, j, temp;
    scanf("%d", &n);
    int a[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        for (j = 0; j < i; j++)
        {
            if (a[i] == a[j])
            {
                printf("Invailed");

                exit(0);
            }
        }
    }
    scanf("%d", &value);
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n - 1; j++)
        {
            if (a[i] > a[j])
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
    printf("%d", a[n - value]);
    // int count = 1;
    // int temp;
    // scanf("%d", &n);
    // if (n < 0)
    // {
    //     printf("Worng Input");
    //     return 0;
    // }

    // temp = n;
    // while (temp != 0)
    // {
    //     temp = temp / 10;
    //     count = count * 10;
    // }

    // if (n == ((n * n * n * n) % count))
    // {
    //     printf("True");
    // }
    // else
    // {
    //     printf("False");
    // }
    return 0;
}