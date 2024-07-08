# Windows

```sh
# 用户名排查
wmic useraccount get name,sid
## 3.影子用户：只有注册表中能看到
$lines = (wmic useraccount get name,sid | Select-Object -Skip 1 | Measure-Object -Line).lines
$Key="hklm:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"
$user_reg=$(Get-ChildItem -path $Key).length
$res = $lines - $user_reg
# echo "影子账户数量 $($lines - $shadow)"
echo "影子账户数量 $res"

netstat -ano
netstat -ano|findstr ESTABLISHED

tasklist

# 内存中的进程, 带路径
wmic process get name,executablepath

# 日志
%SystemRoot%\System32\Winevt\Logs\Application.evtx
%SystemRoot%\System32\Winevt\Logs\Security.evtx
%SystemRoot%\System32\Winevt\Logs\System.evtx

# 计划任务
Get-ScheduledTask | % { $_.taskname +","+  $_.Actions.execute }

dir /a "C:\Documents and Settings"
dir %UserProfile%\AppData\Roaming\Microsoft\Windows\Recent
dir C:\Users\default\AppData\Roaming\Microsoft\Windows\Recent

# 启动程序
dir "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
reg export HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run HKLM_RUN.reg
reg export HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce HKLM_runonce.reg
reg export HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run HKCU_run.reg
```

## 日志排查/Windows

```sh
eventvwr.msc
```

### evtx

[evtx](https://blog.csdn.net/administratorlws/article/details/139887217)

[logParser](win_11_log_logParser.md)

找到关键“登录”，事件 ID 4624

| ID            | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| 事件 ID 4624  | 成功的账户登录                                                       |
| 事件 ID 4625  | 登录失败                                                             |
| 事件 ID 4634  | 用户注销                                                             |
| 事件 ID 4647  | 用户主动注销                                                         |
| 事件 ID 4720  | 用户账户已创建                                                       |
| 事件 ID 4722  | 用户账户已启用                                                       |
| 事件 ID 4725  | 用户账户已禁用                                                       |
| 事件 ID 4726  | 用户账户已删除                                                       |
| 事件 ID 4670  | 权限服务状态变更                                                     |
| 事件 ID 4719  | 系统审计策略已更改                                                   |
| 4648          | 试图使用明确的凭证登录（可以查看远程登陆的相关信息，比如 IP 地址等） |
| \* 系统事件   | -------------------                                                  |
| 事件 ID 6005  | 事件日志服务启动                                                     |
| 事件 ID 6006  | 事件日志服务停止                                                     |
| 事件 ID 6008  | 系统意外关机                                                         |
| 事件 ID 4672  | 特权服务已分配                                                       |
| 事件 ID 4673  | 特权服务已请求                                                       |
| \* 防火墙事件 | -------------------                                                  |
| 事件 ID 4946  | Windows 防火墙规则添加                                               |
| 事件 ID 4947  | Windows 防火墙规则修改                                               |
| \* 文件访问   | -------------------                                                  |
| 事件 ID 4663  | 记录对象访问尝试的安全审计事件                                       |
| \* 服务状态   | -------------------                                                  |
| 事件 ID 7036  | 服务已更改状态（如启动或停止）                                       |

## 进程排查

```sh
msinfo32，依次点击“软件环境→正在运行任务”
Process Explorer
火绒剑（HRSword.exe），开启监控，重点关注没有签名信息的进程。
```

## 服务排查

```ps1
# Import-Module -Name CimCmdlets
$services = Get-WmiObject -Class Win32_Service | Select-Object -Property Name, DisplayName, PathName
$services | Export-Csv -Path "services.csv" -NoTypeInformation -Encoding UTF8
```

[服务排查脚本完善 | Windows 应急响应](https://mp.weixin.qq.com/s/_OLwgWbrnAhXLGdc0n_Kaw)

## 组策略

```sh
#只允许超级管理员（administrator）关闭操作系统
管理工具 -> 本地安全策略 ->  本地策略 -> 用户权限分配 ->关闭系统 删除其他用户

#设置远程桌面用户空闲会话超过5分钟自动断开连接
win+r-gpedit.msc -> 计算机配置 -> 管理模板 -> Windows 组件 -> 远程桌面服务 -> 远程桌面会话主机-> 会话时间限制 > 设置活动但空闲的远程桌面服务会话的时间限制 10分钟
## 值为秒支持16进制 0x000927c0
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v MaxIdleTime /t reg_dword /d 600000 /f

#开启开启IIS的日志审计记录
服务器管理 -> 用户  -> Web服务器IIS -> 角色服务 添加角色服务 -> 健康与诊断 -> 勾选HTTP日志记录

#九、 ftp安全 关闭ftp匿名用户（注意ftp服务不能关闭）
控制面板 -> 管理工具 -> IIS管理器 -> ftp身份验证禁用匿名用户
```
