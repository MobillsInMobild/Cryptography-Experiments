#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
void sieveOfEratosthenes(int n);
void sieveOfEratosthenes_Recursion(int n);
void sieveOfEuler(int n);

int list2[10000000];
int main()
{
    clock_t startTimeFirst, endTimeFirst, startTimeSecond, endTimeSecond, startTimeThird, endTimeThird;
    int n;
    scanf("%d", &n);
    startTimeFirst = clock();
    sieveOfEratosthenes(n);
    endTimeFirst = clock();
    printf("\n sieveOfEratosthenes:CPU 占用的总时间：%lf\n", (double)(endTimeFirst - startTimeFirst) / CLOCKS_PER_SEC);

    startTimeSecond = clock();
    for (int i = 2; i <= n; i++)
    {
        list2[i] = 1;
    }
    sieveOfEratosthenes_Recursion(n);
    // for (int i = 2; i <= n; i++)
    // {
    //     if (list2[i] == 1)
    //     {
    //         printf("%d ", i);
    //     }
    // }
    endTimeSecond = clock();
    printf("\n sieveOfEratosthenes_Recursion:CPU 占用的总时间：%lf\n", (double)(endTimeSecond - startTimeSecond) / CLOCKS_PER_SEC);

    startTimeThird = clock();
    sieveOfEuler(n);
    endTimeThird = clock();
    printf("\n sieveOfEuler:CPU 占用的总时间：%lf\n", (double)(endTimeThird - startTimeThird) / CLOCKS_PER_SEC);

    return 0;
}

/*
sieve of Eratosthenes
list为数表
list[i]=1时表示数在表中
list[i]=0时表示数已经被划去
*/
void sieveOfEratosthenes(int n)
{
    int* list1;
    list1=(int*)malloc((n+1)*sizeof(int));
    for (int i = 0; i <= n; i++)
    {
        list1[i] = 1;
    }
    for (int i = 2; i * i <= n; i++)
    {
        if (list1[i] == 1)
        {
            for (int j = i; i * j <= n; j++)
            {
                list1[i * j] = 0;
            }
        }
    }
    // for (int i = 2; i <= n; i++)
    // {
    //     if (list1[i] == 1)
    //     {
    //         printf("%d ", i);
    //     }
    // }
    return;
}

/*
sieve of Eratosthenes_Recursion
[2,N]中的素数，都会由[2,sqrt(N)]筛选出来
因此，运用递归，可以得到[2,sqrt(N)]，然后就可以得到[2,N]中的素数
list为素数表
list[i]=1时表示数在表中
list[i]=0时表示数已经被划去
*/
void sieveOfEratosthenes_Recursion(int n)
{
    if (n == 2)
    {
        list2[2] = 1;
    }
    else
    {
        sieveOfEratosthenes_Recursion(((int)sqrt(n)) + 1);
        for (int j = 2; j * j <= n; j++)
        {
            if (list2[j] == 1)
            {
                for (int k = j; k * j <= n; k++)
                {
                    list2[k * j] = 0;
                }
            }
        }
    }
    return;
}

/*
sieve of Euler
每一个合数都是由其最大因子与最大因子的最小素因子之积
prime是素数表，pnum是素数的个数
list是数表
*/
void sieveOfEuler(int n)
{
    int *list3;
    list3 = (int *)malloc((n+1) * sizeof(int));
    int *prime;
    prime = (int *)malloc((n+1) * sizeof(int));
    int pnum = 0;
    for (int i = 2; i <= n; i++)
    {
        list3[i] = 1;
    }
    for (int i = 2; i <= n; i++)
    {
        if (list3[i] == 1)
        {
            prime[pnum++] = i;
        }
        for (int j = 0; prime[j] * i <= n && j < pnum; j++)
        {
            list3[prime[j] * i] = 0;
            if (i % prime[j] == 0)
            {
                break;
            }
        }
    }
    // for (int i = 0; i < pnum; i++)
    // {
    //     printf("%d ", prime[i]);
    // }
    return;
}