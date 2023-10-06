
* 1.使用错误流 stderr
```sh
sh flag
# sh <filename> 会直接显示文件内容
```

* 2.重定向
```sh
exec 1>&2
cat flag
```
