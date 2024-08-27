

[TOC]

sh=process() 本地连接

sh=remote(ip,port) 远程连接

sh.send(data) 发送数据

sh.sendline(data) 发送一行数据

sh.recv(numb,timeout) 接收数据，指定数量与超时时间

sh.recvline(keepends) 接收一行数据，是否保留\n

sh.recvuntil(data) 接收知道出现data

sh.recvall() 一直接收到EOF

sh.recvpeat(timeout) 同上

sh.interactive() 交换模式



asm(data,arch) 获取机器码

disasm(data) 获取反汇编

