[TOC]

# API

## mprotect
int mprotect(const void* start,size_t len ,int prot) 
	prot:
		PROT_READ
		PROT_WRITE
		ROCT_EXIT
		PROT_NONE


# ASLR

DLL Characteristics:
	Address:IMAGE_OPTIONAL_HEADER+90/94
	#define IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE 0x0040 // DLL can move. 
	#define IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY 0x0080 // Code Integrity Image
	#define IMAGE_DLLCHARACTERISTICS_NX_COMPAT 0x0100 // Image is NX compatible 
	#define IMAGE_DLLCHARACTERISTICS_NO_ISOLATION 0x0200 // Image understands isolation and doesn't want it 
	#define IMAGE_DLLCHARACTERISTICS_NO_SEH 0x0400 // Image does not use SEH. No SE handler may reside in this image 
	#define IMAGE_DLLCHARACTERISTICS_NO_BIND 0x0800 // Do not bind this image. // 0x1000 // Reserved. 
	#define IMAGE_DLLCHARACTERISTICS_WDM_DRIVER 0x2000 // Driver uses WDM model // 0x4000 // Reserved.
	#define IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE 0x8000
