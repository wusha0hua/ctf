[TOC]

# API Detection

## IsDebuggerPresent
- int IsDebuggerPresent(void)
   - the return value is BeingDeBugged

### Code
- assembly 
```assembly
mov eax ,dword ptr fs:[0x18]
mov eax,dword ptr[eax+0x30]
mov eax,dword ptr[eax+0x2]
```
- C
```c++
#include<stdio.h>
#include<windows.h>
int main()
{
	int a = IsDebuggerPresent();
	if (a == 1)
    {
        puts("Dugging");
    }
    else
    {
        puts("NO");
    }
    getchar();
    return 0;
}
```
	

## NtQueryInformationProcess/ZwNtQueryInformationProcess
NtQueryInformationProcess/ZwNtQueryInformationProcess(in Ntdll.dll)
(
\_In_HANDLE ProcessHandle
\_In_ PROCESSCLASS ProcessClass
\_Out_ PVOID ProcessInformation
\_ In_ ulong ProcessInformationLength
\_Out_Opt_ PULONG ReturnLegth
)

	enum ProcessClass
	{
	…
	DebugPort=0x7
	…
	ProcessDebugHandle=0x1e
	…
	}
	
	when the ProcessClass value is 0x7 and debugging ,ProcessInformation will be 0xffffffff, otherwise will be 0;
	when being 0x1e , PI is the handle of debugged process ,otherwise is 0; 
	

## CheckRemoteDebuggerPresent
void CheckRemoteDebuggerPresent
(
_Int_ HANDLE PROCESSHANDLE
_Out_ bool returnvalue
):
	it can detecte no only itself

### Code
```c++
#include<windows.h>
void main()
{
    PBOOL a;
    CheckRemoteDebuggerPresent(GetCurrentProcess(),a);
    if(a==1)
    {
    exit(0);
    }
}
```
	
	
	

## GetLastError with SetLastError
	
	DWORD GetLastError(void):
		it can get the last error code 
	void SetLastError(DWORD $value):
		set the last error code to $value
	if there are no errors occur after SetLastError it ,the last error code will no change,actively trigger an exception
	
	
## OutputDebugString
void OutputDebugString(char $string):
	put a string in the debugger if there is no debugger it will trigger an exception
	??? : it seems to be invalid
	

## DeleteFiber	
DeleteFiber():
	with an invalid parameter it will trigger a exception that is ERROR_INVALID_PARAMETER(the value is 0x57),if being debugged the exception will be capture
	(???)
	
### Code
- C
```c++
#include<stdio.h>
#include<windows.h>
void fun()
{
	;
}
BOOL CheckDebug()
{
	char fib[1024] = { 0 };
	DeleteFiber(fib);
	return (GetLastError() != 0x57);
}
int main()
{	
	puts("LOCATING");	
	printf("%d", CheckDebug());
	getchar();
}
```
	
## Exception
Cause Exception:
	CloseHandle(),CloseWindow()...
	


# Process Detection

## PEB  
	struct :
		+0x2 BeingDebugged : UChar
		+0x68 NtGlobalFlag : Unit4B
	
	address : x86 : fs:[0x30]
	
	When debugging, BeingDebugged was set 1,else 0; NtGlobalFlag was set 0x70
	
	Crake : jump to fs[0x30/0x68] and overwrite the value to 0

### Code
- c
```c++
#include<stdio.h>
#include<windows.h>
int main()
{
	bool a;
	__asm
	{
		mov eax,dword ptr fs:[0x30]
		mov al,byte ptr [eax+2 ]
		mov a,al
	}
	printf("%d",a);
}
```
	
## TEB
	 
	
STARTUPINFO
	struct:
		omitted
	
	Relevant: 
		CreateProcess
		(
		…
		_Out_ LPSTARTUPINFO LpStartupinfo
		…
		):
		
	when creating a process by explorer,created the STARTUPINFO of process was filled by explorer,  the LpStartupInfo is 0,(and all value in STARUPINFO are 0)(?)
	
	Methodk: check the value of member in STARTUPINFO if they are 0  
	
### Code
- assembly  
```assembly
…
mov eax,dword ptr fs:[0x18] //get TEB address(?)
mov eax,dword ptr [eax+0x30] 
mov ecx,dword ptr [eax+0x10] //get PROCESS_PARAMETERS address
mov eax,dword ptr [eax+8] //get STARTUPINFO address
… 
```

- C
```c++
#include<stdio.h>
#include<windows.h>
void fun()
{
	;
}
BOOL CheckDebug()
{
	CloseHandle((HANDLE)0xffffffff);
	return (GetLastError() != 0x57);
}
int main()
{
	puts("LOCATING");
	STARTUPINFO si;
	GetStartupInfo(&si);
	printf("%d,%d,%d,%d,%d",si.dwFlags,si.dwXSize,si.dwYSize,si.dwY,si.dwX);
	getchar();
}
```
	
## SeDebugPrivilege
	Intruduce:
		when a process was create normally,it can't have privilege to debug,unless it can promote privilege(?),however the dubugger have this privilege ,when created by debugger and it will inherit this privilege ,and check it to see if being debugged.
	
	Method:
		we can check if this process can open the handle of csrss.exe to check, only having privilege for administrator and debuge(SeDubugPrivilege) can open it .this method has a fatal defect that
		if the debugger has no administrator privilege ,it can not work. but most debugger will apply for administrator privilege.
		
	

## ProcessHead
	
	Intruduce:
		In the array there is a undisclosed position ---ProcessHead,it is set the first heap position that loader assign to process. it locate at PEB+0x18 and its first character tell kernel if this heap is created in debugger ,these characters called ForceFlags and Flags 
	Address:
		xp:
			ForceFlags: ProcessHead+0x10
			Flags:ProcessHead+0x0c
		win7x86:
			ForceFlags: ProcessHead+0x44
			Flags:ProcessHead+0x40
			
			
			
## NtGlobalFlags
	
	Address:
		PEB+0x68
	if it value is 0x70(FLG_HEAP_ENABLE_TAIL_CHECK|FLG_HEAP_ENABLE_FREE_CHECK|FLG_HEAP_VALIDATE_PARAMETERS) it is in debuuger

### Code
- C
```c++
#include<stdio.h>
#include<windows.h>
int main()
{
	int a;
	__asm
	{
		mov eax,dword ptr fs:[0x30]
		mov eax,dword ptr [eax+0x68 ]
		mov a,eax
	}
	printf("%d",a);
}
```
	
	
	
	
## STL
	
	Intruduce:
		
	
# Enviornment Detection

## Registry Detection
	
	Intruduce:
		when something wrong with the program,system will post a window to user to choose whether to stop or debug,if choose to dubug user should set a jet dubugger and system will write this debugger name in registry.to check registry .default is Dr.Waston
	 Address :
		x86: HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug
		x64:HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\AeDebug
		
	Crack:
		search string --'Aebug' and overwrite it to 0
		
		
## Window Detection
	
	Intruduce:
		when running debugger ,there will be a window for this debugger ,to search it.
	Relevant:
		use API to find window:
			FindWindow()
			EnumWindow()
			GetForegroundWindow()
			(?)
	Method: search debugger name that may be used  
	Crack:  in the debugger search the debugger name that you using and overwrite it to 0

### Code
- C
```c++
#include<stdio.h>
#include<windows.h>
int main()
{
	int a;
	HANDLE p = NULL;
	p=FindWindow(NULL,TEXT("x32dbg"));
	if (p != NULL)
	{
		puts("Being");
	}
	getchar();
}
```


## Father Process Detection

	Intruduce:
		if a process is not created by debugger ,it is created by explorer , check its father process if it is explorer.exe
	Method :
		use NtQueryInformationProcess() to get father process id and traverse all process id and find the process id is equal to father process id ,if its name is not explorer.exe …
		or get the explorer.exe's id and check it if is equal to father process ,but this method has a fatal defect that if there is not only one explorer.exe is running it may wrong.
		this method error rate is high.
	Crack : 
		rename you debugger to explorer.exe



## Scanning Process
	
	Intruduce:
		scan all process is running and see if there is a sensitive process
		
	Crack:
		rename
		


## Scaning Kernel Object
	
	Intruduce:
		when debugging ,system will create a kernel object class named DebugObject 
	Method:
		seach kernel object linked list to find if there is a class named DebugObeject
	Crack: 
		search string --'DebugObject' and  overwrite it with 0



## Debug Model Detection
	
	Intruduce:
		???
		


## Debugger Attack
	
	Intruduce:
		call ZwSetThreadInformation() with parameter ThreadHideFromDebugger can make current thread out of debugger ,if there is no debugger ,it makes nothing
	Relevant:
		ZwSetThreatInformation
		(
		
		)
		
		enum
		{
			…
			ThreadHideFromDebbger=17
			…
		}
	Crack: API Hook
	
	
	
	
	
	
## In Instruction
	
	Intruduce:
		between Vmware and real machine have communication mechanism , it depends on in instruction to get specific port to get data ,you can use in instruction to get the information, but in instruction is a privileged instruction and if it is used in real machine it will trigger an exception -- EXCEPTION_PRIV_INSTRUCTION , however in virtual machine will not trigger that exception


# Clock Detection

## CPU Counter
	
	Intruduce:
		when running in debugger ,the code runs slowlier than runs in real environment
	Relevant:
		x86:
			_64b_REG_ TSC :uesd to save clock count
			_assembly_  RDTSC/RDTSCP :  load high 32 TSC to edx and low 32 to eax  
	Method:
		use two pieces of code to get clock count and they are close to each other and calculate the difference if the difference is over a specail value it is in debbuger .however the diference can be caused from other reason ,such as thread change

### Code
- C
```c++
#include<stdio.h>
#include<windows.h>
int main()
{
	INT64 t1;
	int hi, lo;
	__asm
	{
		rdtsc
		mov lo,eax
		mov hi,ecx
	}
	t1 = INT64(((INT64)hi<<32)|(INT64)lo);
	printf("%d\n",t1);
	t1 = ReadTimeStampCounter();
	printf("%d", t1);
}
```


## Time API
	
	Relevant:
		QueryPerformanceCounter
		(
		
		)
		GetTickCount
		(
		
		)
		GetSystemTime
		(
		
		)
		GetLocalTime
		(
		
		)
(?)
	Crack:API Hook,but some time API are not just used to anti-debuge

# Abnorm Detection
## SEH
	
	Relevant:
		common abnorm:
			…
			EXCEPTION_BREAKPOINT    0x80000003
			…
			
	???

### Code
- C 
```c++
#include<stdio.h>
#include<windows.h>
int main()
{
	puts("asdasdasdasdadasd");
	char format[] = "%d";
	bool flag = 0;
	__asm
	{
		push handle
		push dword ptr fs:[0]
		mov  fs:[0],esp
		_emit(0xcc)
		mov flag,1
		jmp normalcode
	handle:
		mov eax, dword ptr ss : [esp + 0xc]
		mov dword ptr ds:[eax+0xb8],offset normalcode
		xor eax,eax
		push format
		call printf
		retn
	normalcode:
		pop dword ptr fs:[0]
		add esp,4
	}			
}
```


## SetUnhandledExceptionFilter()
	
	???
	
	


Indirecion Abnorm Detection:
	
	Intruduce:
not use SEH but use CONTEXT to check


### Code 
- C
```c++
#include<stdio.h>
#include<windows.h>
LONG WINAPI fun()
{
	printf("666");
	return 1;
}
int main()
{
	puts("asdasdasdasdadasd");
	bool flag = 0;
	SetUnhandledExceptionFilter((LPTOP_LEVEL_EXCEPTION_FILTER)fun);
	__asm 
	{
	    _emit(0xcc)
	    xor eax,eax
	}
	getchar();
}
```

# Breakpoint Detection

## Int 2d Breakpoint
	
	Intruduce:
		this breakpoint has some special feature. when process running without debugger ,and coming to int 2d breakpoint, the process will ignore it .when running in a debugger ,it will not cause a interruption but will omit the next machine code and wiil not stop at the next step and go throug .it also will not trigger SEH abnorm and set bDebugging to 1 but if not in debugger it will trigger SEH  and set bDebugging to 0

## 0xcc Breakpoint
	
	Intruduce:
		nothing
	Method:
		detecte a position that probably will be set a 0xcc breakpoint if it is 0xcc

### Code 
- C
```c++
#include<stdio.h>
#include<windows.h>
void fun()
{
	puts("sdsdsd");
}
int main()
{
	puts("asdasdasdasdadasd");
	fun();
	int a;
	PBYTE p = (PBYTE)fun;
	if (*p == 0xcc)
	{
		puts("Yes");
	}
	else
	{
		puts("No");
	}
}
```




## Double 0xcc Breakpoint
	
	Intruduce:use CD 03 to interfere WinDbg
		
		
		
		???


## Code Check
	
	Intruduce:
		if there are some software breakpoint in a piece of code ,they will change the code a little
	Method:
		you can add the machine code of a piece of code at the beginning ,than do more one time in that code ,compare the two sum if they are same ,but this method may not work if there is no new breakpoint added
		or you can calculate by youself and check if the sum is the same

### Code
- C
```c++
#include<stdio.h>
#include<windows.h>
void fun()
{
	puts("sdsdsd");
}

int main()
{
	puts("asdasdasdasdadasd");
	int a=0,i=0,sum=0;
	PBYTE p,q;
	__asm
	{
		xor eax,eax
		call o
	o:
		pop eax
		mov p,eax
	}
	q = p;
	for (i = 0; i < 30; i++)
	{
		a += (int)*(p + i);
	}
	sum = a;
	for (a=0,i = 0, p = q; i < 30; i++)
	{
		a += (int)*(p + i);
	}
	if (a != sum)
	{
		printf("YEs");
	}
	else
	{
		printf("NO");
	}
}
```



## Hard Breakpoint
	
	Intruduce:
		if they don't use software breakpoint
	Relevant:
		hard breakpoint is relevant to register Dr0~Dr7, and Dr0~Dr3 is used to save hard brekpoint address, Dr4 and Dr5 are unkwon, Dr6 and Dr7 save relevant character(?), use API to get value
		CONTEXT:
			struct:
				(?)
		CONTEXT $name.ContxetFlags=CONTEXT_DEBUG_REGISTERS(?)
		$name.Dri %i for i in range(0,8)
	Crack: hook GetThreadContext, change $name.ContextFlags to CONTEXT_INTERGER(0x10002)(?)

### Code
- C
```c++
#include<stdio.h>
#include<windows.h>
void fun()
{
	puts("sdsdsd");
}
int main()
{
	puts("asdasdasdasdadasd");
	CONTEXT context;
	HANDLE ht=GetCurrentThread();
	context.ContextFlags = CONTEXT_ DEBUG_REGISTERS;
	GetThreadContext(ht, &context);
	printf("%d\n%d\n%d\n%d\n",context.Dr0,context.Dr1,context.Dr2,context.Dr3);
	getchar();
}
```
	
# Single Step Detection

## call/rep Step By
	
	Intruduce:
		when go to call or rep instruction ,some of them have no need to step in ,if step by ,the next code will become 0xcc and detecte it or change it to nop let ip go away 
	???

### Code
```c++
#include<stdio.h>
#include<windows.h>
void fun()
{
	puts("sdsdsd");
}

int main()
{
	puts("asdasdasdasdadasd");
	int flag = 0;
	__asm
	{
	xor eax,eax
	xor ecx,ecx
	inc ecx
	lea esi,key
	rep lobsb
key:
	cmp al,0xcc
	je debug
	jmp over
debug:
	mov flag,1
over:	
	}
	printf("%d",flag);
	getchar();
}
```
	
	
## TF Detection
	
	Intruduce:
		when single step ,TF will be 1 than trigger a breakpoint interruption it will be set 0
		
		
# Self-Debug

# Debuuger Bug

## PE_Header Bug
	
	Instruction:
		in the optional header there is a character named NumberOfRvaAndSizes it is used to save number of DataDirectory array, the DataDirectory has two member--Virtual Address and Sizes ,but their amount will not large than 0x10,when it larger than 0x10  the windows system will ingore it , but in debugger it will make Ollydbg wrong and post "Bad or unknown format of 32-bit executable file"
		
		
		
		
## Section_Header Bug

	Intruduce:
		in the IMAGE_SECTION_HEADER there are VirtualSize and SizeOfRawData, windows loader will choose the smaller one to load in memory but the ollydbg will just load SizeOfRawData so set it as a large data it will make olldbg wrong
		
		
		
		
## OutputDebugString
	
	Intruduce:
		use format string vulnerability OutputDebugString("%s%s%s%s") to make ollydbg crash



# TLS

Define:
	typedef VOID (WINAPI *PIMAGE_TLS_CALLBACK)
	(
		PVOID DllHandle,
		DWORD Reason,
		PVOID Reserved
	)
	
	Reason:
		#define DLL_PROCESS_ATTACH  1
		#define DLL_THREAD_ATTACH   2
		#define DLL_THREAD_DETACH   3
		#define DLL_PROCESS_DETACH  4
		





## Code
- C
```c++
#include<windows.h>
#include<stdio.h>

#pragma comment(linker,"/INCLUDE:__tls_used")

	void print_console(char* szMsg)
{
	HANDLE hstdout = GetStdHandle(STD_OUTPUT_HANDLE);
	WriteConsoleA(hstdout, szMsg, strlen(szMsg), NULL, NULL);
}

void NTAPI TLS_CALLBACK1(PVOID DllHandle, DWORD Reason, PVOID Reserved)
{
	char szMsg[80] = { 0, };
	wsprintfA(szMsg, "TLS_CALLBACK1():DLLHandle=%x,Reason=%d\n", DllHandle, Reason);
	print_console(szMsg);
}

void NTAPI TLS_CALLBACK2(PVOID DllHandle, DWORD Reason, PVOID Reserved)
{
	char szMsg[80] = { 0, };
	wsprintfA(szMsg, "TLS_CALLBACK2():DLLHandle=%x,Reason=%d\n", DllHandle, Reason);
	print_console(szMsg);
}

#pragma data_seg(".CRT$XLX")
PIMAGE_TLS_CALLBACK pTLS_CALLBACKs[] = { TLS_CALLBACK1,TLS_CALLBACK2,0 };
#pragma data_seg()

DWORD WINAPI ThreadProc(LPVOID lparam)
{
	print_console("ThreadProc(): start\nThreadProc(): end\n");

	return 0;
}

int main()
{
	HANDLE hthrd = NULL;
	print_console("main(): start\n");
	hthrd = CreateThread(NULL, 0, ThreadProc, NULL, 0, NULL);
	WaitForSingleObject(hthrd, 1000 * 60);
	CloseHandle(hthrd);
	print_console("main(): end\n");
	return 0;
}
```

# SMC

\#pragma data_seg("share")
int val=5
\#pragma data_seg()
//create a shared data segment named share, the data that are initialized will be put in segment named share ,if the data is uninitailized data ,it will be put in .bss segment and it will not be shared 

\#pragma comment(linker, "/SECTION:.share,ERW")
//add the share segment . E:executable R:readable W: writable S:sharable


typedef struct _IMAGE_SECTION_HEADER {
    BYTE    Name[IMAGE_SIZEOF_SHORT_NAME];
    union {
            DWORD   PhysicalAddress;
            DWORD   VirtualSize;
    } Misc;
    DWORD   VirtualAddress;
    DWORD   SizeOfRawData;
    DWORD   PointerToRawData;
    DWORD   PointerToRelocations;
    DWORD   PointerToLinenumbers;
    WORD    NumberOfRelocations;
    WORD    NumberOfLinenumbers;
    DWORD   Characteristics;
} IMAGE_SECTION_HEADER, *PIMAGE_SECTION_HEADER;

Characteristics:
	0x00000020:this is a code segment
	0x00000040:this segment includes initialized data
	0x00000080:this segment includes uninitailized data
	0x02000000:the data in this segment can be remove
	0x10000000:this segment can executable
	0x20000000:this segmemt is shared
	0x40000000:this segment is readable
	0x80000000:this segment is writable

## Code 
- C
```c++
#include<stdio.h>
#include<windows.h>
#pragma code_seg("fun")
int fun(void)
{
	int a;
	__asm
	{
		xor eax, eax
		mov ecx,0
		call jump
		jump:
		pop ecx
		xor [ecx+5],0xA
		_emit(0x4a)
		mov a, eax
	}
	return a;
}
#pragma code_seg()
#pragma comment(linker,"/SECTION:.fun,ERW")
void main()
{
	puts("asdadasdasd");
	char name[8] = "fun";
	IMAGE_DOS_HEADER* pe;
	DWORD s;
	DWORD base;
	pe= (IMAGE_DOS_HEADER*)GetModuleHandle(NULL);
	base = (DWORD)pe;
	PIMAGE_NT_HEADERS ntheader=(PIMAGE_NT_HEADERS)(base+pe->e_lfanew);
	PIMAGE_SECTION_HEADER sectionheader;
	sectionheader = (PIMAGE_SECTION_HEADER)((DWORD)ntheader+sizeof(IMAGE_NT_HEADERS));
	printf("%s\n", sectionheader->Name);
	while (1)
	{
		if (memcmp(sectionheader->Name, name, 8) != 0)
		{
			sectionheader = (PIMAGE_SECTION_HEADER)(40 + (DWORD)sectionheader);
		}
		else
		{
			//sectionheader->Characteristics = sectionheader->Characteristics | 0x80000000;
			s = sectionheader->Characteristics | 0x80000000;
			BOOL re=WriteProcessMemory(GetCurrentProcess(),(LPVOID)sectionheader->Characteristics,(LPVOID)&s,sizeof(DWORD),NULL);
			printf("%x",GetLastError());
			break;
		}
	}
	int a;
	
	printf("%d", fun());
}

```

