#include <stdio.h>
#include <stdlib.h>
void sieveOfEuler(int n);

int list[10000000] = {0};
int main()
{
    int n;
    printf("Please input your n\n");
    scanf("%d", &n);
    sieveOfEuler(n);
    return 0;
}


/*
sieve of Euler
每一个合数都是由其最大因子与最大因子的最小素因子之积
prime是素数表，pnum是素数的个数
list是数表
*/
void sieveOfEuler(int n)
{
    int* prime;
    prime=(int*)malloc(n*sizeof(int));
    int pnum = 0;
    for (int i = 2; i <= n; i++)
    {
        list[i] = 1;
    }
    for (int i = 2; i <= n; i++)
    {
        if (list[i] == 1)
        {
            prime[pnum++] = i;
        }
        for (int j = 0; prime[j]*i<=n&&j < pnum; j++)
        {
            list[prime[j] * i] = 0;
            if (i % prime[j] == 0)
            {
                break;
            }
        }
    }
    for (int i = 0; i < pnum; i++)
    {
        printf("%d ", prime[i]);
    }
    free(prime);
    return;
}