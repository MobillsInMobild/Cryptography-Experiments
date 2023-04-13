#include <math.h>
#include <stdio.h>

void sieveOfEratosthenes(int n);
int main()
{
    int n;
    printf("Please input your n\n");
    scanf("%d", &n);
    sieveOfEratosthenes(n);
    return 0;
}



/*
sieve of Eratosthenes
list为素数表
list[i]=1时表示数在表中
list[i]=0时表示数已经被划去
*/
void sieveOfEratosthenes(int n)
{
    int list[100000]={0};
    for (int i = 0; i <= n;i++){
        list[i] = 1;
    }
        for (int i = 2; i*i <=n; i++)
        {
            if (list[i] == 1)
            {
                for (int j = i; i * j <= n; j++)
                {
                    list[i * j] = 0;
                }
            }
        }
    for (int i = 2; i <= n; i++)
    {
        if (list[i] == 1)
        {
            printf("%d ", i);
        }
    }
    return;
}