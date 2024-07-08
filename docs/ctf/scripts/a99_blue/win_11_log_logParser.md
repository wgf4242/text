# Log Parser

下载地址：https://www.microsoft.com/en-us/download/details.aspx?id=24659

[Example](https://mlichtenberg.wordpress.com/2011/02/03/log-parser-rocks-more-than-50-examples/)
[『工具使用』日志分析工具之 LogParser](https://mp.weixin.qq.com/s/8QzI8nOYdRev4YZxGRNK6A)

```sh
path "C:\Program Files (x86)\Log Parser 2.2";%path%
$env:path="C:\Program Files (x86)\Log Parser 2.2";$path
LogParser.exe -i:EVT -o:DATAGRID -q:ON "SELECT TOP 50 * FROM Security.evtx where (EventID=4624 OR EventID=4625 or EventID=4634) ORDER BY TimeGenerated DESC"
LogParser.exe -i:EVT -o:DATAGRID "SELECT * FROM E:\Security.evtx where EventID=4624"
LogParser.exe -i:EVT -o:DATAGRID "SELECT * FROM F:\Security.evtx WHERE EventID=4624 ORDER BY TimeGenerated DESC"
LogParser.exe -i:EVT -o:DATAGRID "SELECT * FROM Security.evtx WHERE EventID=4648 ORDER BY TimeGenerated DESC"
LogParser.exe -i:EVT -o:DATAGRID "SELECT * FROM F:\Security.evtx WHERE EventID=4624 OR EventID=4625 ORDER BY TimeGenerated DESC"
LogParser.exe -i:EVT -o:DATAGRID "SELECT * FROM Security.evtx where (EventID=4624 OR EventID=4625) AND Message LIKE '%源网络地址%'  ORDER BY TimeGenerated DESC"
LogParser.exe -i:EVT -o:DATAGRID "SELECT * FROM Security.evtx where (EventID=4624 OR EventID=4625 or EventID=4634) AND Message LIKE '%源网络地址%'  ORDER BY TimeGenerated DESC"

logparser file:XXXXX.sql
logparser "SELECT * into OUTPUT.CSV FROM Security.evtx"
```

| id   | desc                   |
| ---- | ---------------------- |
| 4624 | 帐户已成功登录         |
| 4625 | 帐户登录失败           |
| 4648 | 试图使用明确的凭证登录 |

- Windows 下审核进程创建教程

```sh
打开“本地组策略(gpedit.msc)”，左侧列表打开“计算机配置——Windows 设置——安全设置——高级审核策略配置——系统审核策略——详细跟踪”，右侧双击“审核进程创建”，把配置“成功”和“失败”勾上。至此，审核进程创建已经配置完毕。
```

# Article

[windows 日志一键分析工具](https://mp.weixin.qq.com/s/XWxueZSptXeFZU3DpoLCew)
