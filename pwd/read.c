#include<unistd.h>
#include<stdio.h>
#include<string.h>

int main()
{
    int b;
    char buf[5];
    int a;
    char buf2[5];
    int c;
    memset(buf,0,5);
    memset(buf2,0,5);
    //scanf("%d",&a);
    //read(1,buf,5);
    //scanf("%s",buf);
    read(0,buf,5);
    printf("%s\n------------------------------------------\n",buf);
    int i=0;
    while(i<20)
    {
        printf("0x%X ",*(char*)(buf+i));
        i++;
    }
    puts("");
    // printf("\n%ld\n",strlen(buf));
    // printf("%p\n",&a);
    // printf("%p\n",&b);
    // printf("%p\n",&c);
    // printf("%p\n",buf);
    // printf("%p\n",buf2);
    // FILE* fp=fopen("txt.txt","w");
    // size_t j=write(fp,buf,1000000);
    // puts("");
    // printf("%lud\n",j);
    size_t j=1;
    printf("%lud\n",sizeof(long int));
}