#include <math.h>
#include <stdio.h>

void sieveOfEratosthenes_Recursion(int n);

int list[10000000] = {0};
int main()
{
    int n;
    printf("Please input your n\n");
    scanf("%d", &n);
    for (int i = 2; i <= n; i++)
    {
        list[i] = 1;
    }
    sieveOfEratosthenes_Recursion(n);
    for (int i = 2; i <= n; i++)
    {
        if (list[i] == 1)
        {
            printf("%d ", i);
        }
    }
    return 0;
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
        list[2] = 1;
    }
    else
    {
        sieveOfEratosthenes_Recursion(((int)sqrt(n)) + 1);
        for (int j = 2; j * j <=n;j++)
        {
            if (list[j] == 1)
            {
                for (int k = j; k * j <= n; k++)
                {
                    list[k * j] = 0;
                }
            }
        }
    }
    return;
}