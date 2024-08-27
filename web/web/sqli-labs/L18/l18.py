import requests

url="http://localhost/sqli-labs-master/Less-18"
header={'User-Agent':'hacked'}
param={'uname':'admin','passwd':'admin'}
r=requests.post(url,headers=header,data=param)


print(r.text)
