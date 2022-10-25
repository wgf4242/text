echo HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\names\%username%  [1 5 7 11 17]>>access.ini

@echo off
setlocal EnableDelayedExpansion

for /f "delims=" %%i in ('reg query "HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users"') do (
   set "myPath=%%i"
   for /f "delims=" %%j in ("!myPath!") do set "name=%%~nxj"
   echo !name!
   echo HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\!name!  [1 5 7 11 17]>>access.ini
)

regini access.ini
reg delete "HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\    (默认)    REG_LINK" /f

reg export HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\names\%username% export.reg /f
