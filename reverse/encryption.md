[TOC]

#Base64


## Code
### C
```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    char s[100]={0};
    char *base=NULL;
    scanf("%s",s);
    int l1=strlen(s);
    int l2;
    if(l1%3==0)
    {
        l2=l1/3*4;
    }
    else
    {
        l2=(l1/3+1)*4;
    }
    
    base=(char*)malloc(l2);
    int i=0;
    for(i=0;i<l1/3+1;i+=1)
    {
        base[i*4]=((s[i*3]&0xfc)>>2)&0x3f;
        base[i*4+1]=(((s[i*3]&0x3)<<4)&0x30)|(((s[i*3+1]&0xf0)>>4)&0xf);
        base[i*4+2]=(((s[i*3+1]&0xf)<<2)&0x3c)|(((s[i*3+2]&0xc0)>>6)&0x3);
        base[i*4+3]=(s[i*3+2]&0x3f);
    }
    puts(base);
}
```


# Blowfish