[TOC]

# HOOK 

```c++
#include<windows.h>
BOOL start(LPDEBUG_EVENT pde);
BOOL deal(LPDEBUG_EVENT pde);
LPVOID handle;
CREATE_PROCESS_DEBUG_INFO info;
BYTE c = 0xcc;
BYTE old = 0;
void main()
{
	DWORD pid = 232400;
	DebugActiveProcess(pid);

	DEBUG_EVENT de;
	DWORD status;
	while (WaitForDebugEvent(&de, INFINITE))
	{
		status = DBG_CONTINUE;
		if (de.dwDebugEventCode == CREATE_PROCESS_DEBUG_EVENT)
		{
			start(&de);
		}
		else if (de.dwDebugEventCode == EXCEPTION_DEBUG_EVENT)
		{
			if (deal(&de))
				continue;
		}
		else if (de.dwDebugEventCode == EXIT_PROCESS_DEBUG_EVENT)
		{
			break;
		}
		ContinueDebugEvent(de.dwProcessId, de.dwThreadId, status);
	}
}

BOOL start(LPDEBUG_EVENT pde)
{
	handle = GetProcAddress(GetModuleHandle(L"user32.dll"), (LPCSTR)"MessageBoxW");
	memcpy(&info, &pde->u.CreateProcessInfo, sizeof(CREATE_PROCESS_DEBUG_INFO));
	ReadProcessMemory(info.hProcess, handle, &old, sizeof(BYTE), NULL);
	WriteProcessMemory(info.hProcess, handle, &c, sizeof(BYTE), NULL);
	return TRUE;
}
BOOL deal(LPDEBUG_EVENT pde)
{
	CONTEXT ctx;
	PBYTE lpbuffer = NULL;
	DWORD write, text, title, i;
	LPCWSTR s = L"NO";
	
	PEXCEPTION_RECORD per = &pde->u.Exception.ExceptionRecord;
	if (per->ExceptionCode == EXCEPTION_BREAKPOINT)
	{
		if (handle == per->ExceptionAddress)
		{
			WriteProcessMemory(info.hProcess, handle, &old, sizeof(BYTE), NULL);
			ctx.ContextFlags = CONTEXT_CONTROL;
			GetThreadContext(info.hThread, &ctx);
			//ReadProcessMemory(info.hProcess,(LPVOID)(ctx.Esp+0x8),&title,sizeof(DWORD),NULL);
			//ReadProcessMemory(info.hProcess, (LPVOID)(ctx.Esp + 0xC), &text, sizeof(DWORD), NULL);
			WriteProcessMemory(info.hProcess, (LPVOID)(ctx.Esp + 0x8), (LPVOID)s, sizeof(DWORD), NULL);
			WriteProcessMemory(info.hProcess, (LPVOID)(ctx.Esp + 0xC), (LPVOID)s, sizeof(DWORD), NULL);
			ctx.Eip = (DWORD)handle;
			SetThreadContext(info.hThread, &ctx);
			ContinueDebugEvent(pde->dwProcessId, pde->dwThreadId, DBG_CONTINUE);
			Sleep(1);
			WriteProcessMemory(info.hProcess, handle, &c, sizeof(BYTE), NULL);
			return TRUE;
		}
		return FALSE;
	}
}
```

# IAT HOOK

# SSDT HOOK

# INLINE HOOK

# IDT HOOK

# EAT HOOK

# IRP HOOK  