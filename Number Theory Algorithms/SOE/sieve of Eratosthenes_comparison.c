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
    printf("\n sieveOfEratosthenes:CPU ռ�õ���ʱ�䣺%lf\n", (double)(endTimeFirst - startTimeFirst) / CLOCKS_PER_SEC);

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
    printf("\n sieveOfEratosthenes_Recursion:CPU ռ�õ���ʱ�䣺%lf\n", (double)(endTimeSecond - startTimeSecond) / CLOCKS_PER_SEC);

    startTimeThird = clock();
    sieveOfEuler(n);
    endTimeThird = clock();
    printf("\n sieveOfEuler:CPU ռ�õ���ʱ�䣺%lf\n", (double)(endTimeThird - startTimeThird) / CLOCKS_PER_SEC);

    return 0;
}

/*
sieve of Eratosthenes
listΪ����
list[i]=1ʱ��ʾ���ڱ���
list[i]=0ʱ��ʾ���Ѿ�����ȥ
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
[2,N]�е�������������[2,sqrt(N)]ɸѡ����
��ˣ����õݹ飬���Եõ�[2,sqrt(N)]��Ȼ��Ϳ��Եõ�[2,N]�е�����
listΪ������
list[i]=1ʱ��ʾ���ڱ���
list[i]=0ʱ��ʾ���Ѿ�����ȥ
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
ÿһ�����������������������������ӵ���С������֮��
prime��������pnum�������ĸ���
list������
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