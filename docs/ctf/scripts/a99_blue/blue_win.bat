:: # firewall ����ɾ��������վ���򣬸���Ҫ�󿪷��������
netsh advfirewall set allprofiles state on
netsh advfirewall firewall delete rule name="blueteamTCP"
netsh advfirewall firewall delete rule name="blueteamUDP"
netsh advfirewall firewall add rule name="blueteamTCP" dir=in protocol=tcp localport=139,445 action=block
netsh advfirewall firewall add rule name="blueteamUDP" dir=in protocol=udp localport=137,138 action=block

:: # user account
::net user guest  /active:no /domain
net user guest /active:no
net user > user.txt

:: ## export cfg
:: secedit.exe /export /cfg secconfig.cfg
:: import cfg
secedit.exe /configure /db %windir%\securitynew.sdb /cfg .\blue_win.sec.cfg /areas SECURITYPOLICY

net accounts /minpwlen:8
:: ## ��ֹMimikatz��ȡWindows����
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 0
:: ## ����
FOR %%i IN (Browser iphlpsvc RemoteRegistry Server BITS lmhosts WinRM FontCache WinHttpAutoProxySvc WerSvc LPDSVC Spooler) DO sc stop %%i & sc config %%i start= disabled

:: ## �û�Ȩ�޷������: ����Ϊ����Ա�� -- ��Զ��ϵͳǿ�ƹػ�,�ر�ϵͳ,ȡ���ļ����������������Ȩ,�����ص�¼,��������ʴ˼����
:: ### Link https://learn.microsoft.com/zh-cn/windows/security/threat-protection/security-policy-settings/user-rights-assignment
for %%i in (SeNetworkLogonRight SeInteractiveLogonRight SeNetworkLogonRight SeRemoteShutdownPrivilege SeShutdownPrivilege SeTakeOwnershipPrivilege) do (
    for /f %%j in ('wmic useraccount get name') do Ntrights -r %%i -u %%j
    Ntrights -r %%i -u everyone
    Ntrights -r %%i -u Users
    Ntrights +r %%i -u Administrators
)