#!/bin/sh
#修复备份文件泄漏
rm -rf /var/www/html/www.zip

/opt/mssql-tools/bin/sqlcmd -U sa -P "123456" -Q "USE master;

#修复弱口令
ALTER LOGIN sa WITH PASSWORD = 'sasasasa';

#取消授予dbuser模拟sa用户的权限
REVOKE IMPERSONATE ON LOGIN::[sa] FROM [dbuser];

#将dbuser设置为public角色
EXEC sp_addrolemember 'public', 'dbuser';

#修复Trustworthy
ALTER DATABASE industry SET TRUSTWORTHY OFF;
ALTER DATABASE msdb SET TRUSTWORTHY OFF;
ALTER DATABASE master SET TRUSTWORTHY OFF;
GO"

sleep 2