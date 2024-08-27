[TOC]



# 字符型注入



## 判断

```php
$sql="select * from database where id='$id'";
# 先输入$id=1';
# 得到 $sql="select * from database where id='1''";id='1'';如果作为字符会出错
# 输入$id=1"
# $sql="select * from database where id='1"'";作为字符会不出错
```

