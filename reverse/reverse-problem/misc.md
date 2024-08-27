[TOC]

# GUET-CTF2019 re
file format: ELF x64

Mine: 
	search shellpacker : exeinfore.exe -> UPX -> unpack ->use z3 to caculate value 

# V&N2020 CSRe_15
file format: .net

Mine:
	.net -> Ilspy -> encrypted .net -> de4dot ->SHA1 -> to search main funtion

# XCTF firmware
file format: .bin (used in STM32)


# GWCTF2019 xxor
file format :


Focus:
	reverse operation for shift left and shift right


# CKCTF2020 BabyDriver
file format:


Type: maze
Method: see four letter to control if you can get the flag ,and speculate this is a maze.extract maze characters to rebuilda maze 
Focus : some special features for sys file -- the input letter is not depended on the letter shown on the ketboard but depended on the keyboard scancode 

# XCTF findkey

fle format:

Focus: junk code

# XCTF babyre1


Focus: TEA encryption algorithm

# CISCN2018 TryMe

Focus: SIMD ???????????????

# 安洵杯2019 crackme

Mine:
	exception ;unkwon encrytion;

# [ACTF新生赛2020]fungame

# [Zer0pts2020]easy strcmp
s=list("zer0pts{********CENSORED********}")
s1=list(reversed("zer0pts{"))
s2=list(reversed("********"))
s3=list(reversed("CENSORED"))
s4=list(reversed("********"))
for i in range(0,len(s1)):
    print(hex(ord(s1[i])),end="")
print()
for i in range(0,len(s1)):
    print(hex(ord(s2[i])),end="")
print()
for i in range(0,len(s1)):
    print(hex(ord(s3[i])),end="")
print()
for i in range(0,len(s1)):
    print(hex(ord(s4[i])),end="")
print()

p1="0x"+"0x7b0x730x740x700x300x720x650x7a".replace("0x","")
p2="0x"+"0x2a0x2a0x2a0x2a0x2a0x2a0x2a0x2a".replace("0x","")
p3="0x"+"0x440x450x520x4f0x530x4e0x450x43".replace("0x","")
p4="0x"+"0x2a0x2a0x2a0x2a0x2a0x2a0x2a0x2a".replace("0x","")
print(p1)
print(p2)
print(p3)
print(p4)

num1=[0x7b7374703072657a,0x2a2a2a2a2a2a2a2a,0x4445524f534e4543,0x2a2a2a2a2a2a2a2a]
num2=[0,0x410A4335494A0942,0xB0EF2F50BE619F0,0x4F0A3A064A35282B]
num=[0]*4
for i in range(0,4):
    num[i]=hex(num1[i]+num2[i])
print(num)

f1="{stp0rez"
f2="k4m_st3l"
f3="OTED_4_3"
f4="y4d0t_RU"

flag="".join(reversed(f1))+"".join(reversed(f2))+"".join(reversed(f3))+"".join(reversed(f4))+"}"
print(flag)

