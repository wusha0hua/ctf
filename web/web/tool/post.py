import requests

url=input("input url:")

name=input("input param name:")

val=input("input param value:")

mydata={name:val}

r=requests.post(url,data=mydata)

print(r.text)
