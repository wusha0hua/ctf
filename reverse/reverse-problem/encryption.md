[TOC]

# Base64

## WUSTCTF2020 level3

special base64

## [ACTF新生赛2020]usualCrypt

special base64

# SM

## 安洵杯 2019crackMe

SM4

# Tea

## 红帽杯2019 xx

xxtea

## GWCTF2019 xxor

like tea

key=[2,2,3,4]
s=[0xDF48EF7E,0x20CAACF4,0xE0F30FD5,0x5C50D8D6,0x9E1BDE2D,0x84F30420]
j=0
while(j<6):
    i=0
    sun=1166789954*64
    while(i<64):
        s[5-j]-=(s[5-j-1]+sum+20)^((s[5-j-1]<<6)+key[2])^((s[5-j-1]>>9)+key[3])^0x10
        s[5-j-1]-=(s[5-j]+sum+20)^((s[5-j]<<6)+key[0])^((s[5-j]>>9)+key[1])^0x20
        sum-=1166789954
        i+=1
    j+=2  


# Misc

## [FlareOn4]login
rot13:

	s="PyvragFvqrYbtvafNerRnfl@syner-ba.pbz"
	flag=[]
	for x in s:
	    letter=ord(x)
	    if((x>='a' and x<='z') or (x>='A' and x<='Z') ):
	        letter=ord(x)+13
	        if(x<='z' and x>='a' and letter>ord('z')):
	            letter-=26
	        if(x>='A' and x<='Z' and letter>ord('Z')):
	            letter-=26
	    flag.append(chr(letter))
	print("".join(flag))
	
