#include<stdio.h>

void fun()
{
    static int i=0;
    i++;
    if(i>1)
    {
        printf("hacked\n");
    }
    else
    {
        printf("no\n");
    }
}

int main()
{
    char s[15];
    fun();
    gets(s);
    puts(s);
}