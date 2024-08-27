[TOC]

# [ACTF新生赛2020]SoulLike

from pwn import *

table = []
for i in range(128):
    table.append(chr(i))
now = 'actf{'
num = 0
while 1:
    if num == 12:
        break
    for i in table:
        io = process('./SoulLike')
        flag = now + i
        flag = flag.ljust(17,'@')
        flag += '}'
        success(flag)
        io.sendline(flag)
        io.recvuntil('#')
        if num < 9 :
            n = int(io.recv(1))
        else:
            n = int(io.recv(2))
        io.close()
        if n == num + 1:
            now = now + i
            num = num + 1
            break
print num
print now + '}'





from pwn import *
flag="actf{"
num=0
while(1):
        if(num==12):
                break
        for i in range(0,128):
                sh=process("./SoulLike")
                sh.sendline(flag+chr(i)+'}')
                print(flag+chr(i)+'}')
                sh.recvuntil('#')
                if(num<9):
                        numm=int(sh.recv(1))
                else:
                        numm=int(sh.recv(2))
                sh.close()
                if(numm==num+1):
                        print(flag+'}')
                        flag+=chr(i)
                        break
        num+=1
print(flag+'}')



