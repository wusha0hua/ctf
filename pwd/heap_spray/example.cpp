#include <windows.h>
#include <stdio.h>
 
class base
{
	char m_buf[8];
public:
 
	virtual int baseInit1()
	{
		printf("%s\n","baseInit1");
		return 0;
	}
	virtual int baseInit2()
	{
		printf("%s\n","baseInit2");
		return 0;
	}
};
 
 
int main()
{
	unsigned int bufLen = 200*1024*1024;
	base* baseObj = new base;
	char buff[8] = {0};
	char* spray = new char[bufLen];
 
	memset(spray,0x0c,sizeof(char)*bufLen);
	memset(spray+bufLen-0x10,0xcc,0x10);
 
	strcpy(buff,"12345678\x0c\x0c\x0c\x0c");
	baseObj->baseInit1();
 
	return 0;
}