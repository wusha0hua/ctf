[TOC]

VirtualAllocEx
(

)

use LoadLibrary and the dll will run DllMain first and don't use to export function 

```c++
#include<windows.h>
#include<tchar.h>
#include<stdio.h>

int  main()
{
	DWORD pid;
	HANDLE hproc, hthrd;
	HMODULE hmod;
	LPTHREAD_START_ROUTINE lthrd;
	LPDWORD id=NULL;
	
	scanf("%d",&pid);
	hproc = OpenProcess(PROCESS_ALL_ACCESS,0,pid);
	DWORD size = (DWORD)(_tcslen(L"S:\\DLL\\Dll\\Debug\\Dll.dll") + 1) * sizeof(TCHAR);
	LPVOID addr = VirtualAllocEx(hproc,NULL,size,MEM_COMMIT,PAGE_READWRITE);
	WriteProcessMemory(hproc,addr,(LPVOID)L"S:\\DLL\\Dll\\Debug\\Dll.dll",size,NULL);
	hmod = GetModuleHandle(L"kernel32");
	lthrd = (LPTHREAD_START_ROUTINE)GetProcAddress(hmod,"LoadLibraryW");
	hthrd = CreateRemoteThread(hproc,0,0,lthrd,addr,0,id);
	WaitForSingleObject(hthrd,1000);
	CloseHandle(hproc);
}
```

算机\HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows  ????


# direction injection

```c++	
	#include<windows.h>
	#include<tchar.h>
	
	typedef struct
	{
		LPCWSTR user;
		LPCWSTR lib;
		LPCWSTR getprc;
		LPCWSTR fun;
		HANDLE handle;
		LPCWSTR str[2];
		UINT uint;
	
	}Param;
	
	typedef HMODULE(*loadlibrary)(LPCWSTR user);
	typedef FARPROC(*getprocaddress)(HMODULE hmod, LPCWSTR message);
	typedef int (WINAPI*massage)(HANDLE handle,LPCWSTR a, LPCWSTR b,UINT c);
	
	DWORD WINAPI Thread(LPVOID iparam)
	{
		Param* param = (Param*)(iparam);
		HMODULE hmod=((loadlibrary)(param->lib))(param->user);
		HANDLE handle = ((getprocaddress)param->getprc)(hmod,param->fun);
		((massage)handle)(param->handle,param->str[0],param->str[1],param->uint);
		return 0;
	}
	
	int Fun()
	{
		return 1;
		
	}
	
	int  main()
	{
		Fun();
		DWORD pid=202924;
		HANDLE hproc, hthrd;
		HMODULE hmod;
		LPTHREAD_START_ROUTINE lthrd;
		LPDWORD id=NULL;
		LPVOID addr[2];
		DWORD size[2];
		Param param;
		DWORD(WINAPI * thread)(LPVOID lpParam);
		int (*fun)(void);
		fun = Fun;
		thread = Thread;
		
		
	
	
		
		param.user = (LPCWSTR)"user32.dll";
		param.getprc = (LPCWSTR)"GetProcAddress";
		param.lib = (LPCWSTR)"LoadLibrary";
		param.fun = (LPCWSTR)"MessageBox";
		param.handle = NULL;
		param.str[0] = (LPCWSTR)"OK";
		param.str[1] = (LPCWSTR)"OK";
		param.uint = MB_OK;
		//scanf("%d",&pid);
		hproc = OpenProcess(PROCESS_ALL_ACCESS,0,pid);
		size[0] = sizeof(Param);
		addr[0] = VirtualAllocEx(hproc,NULL,size[0],MEM_COMMIT,PAGE_READWRITE);
		WriteProcessMemory(hproc,addr[0],(LPVOID)&param,size[0],NULL);
		size[1] = ((DWORD)fun - (DWORD)thread);
		addr[1] = VirtualAllocEx(hproc,NULL,size[1],MEM_COMMIT,PAGE_READWRITE);
		WriteProcessMemory(hproc,addr[1],(LPVOID)Thread,size[1],NULL);
		hthrd = CreateRemoteThread(hproc,NULL,0,(LPTHREAD_START_ROUTINE)addr[1],addr[0],0,id);
		WaitForSingleObject(hthrd,1000);
		CloseHandle(hproc);
	
	}
```