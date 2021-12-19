@echo off && setlocal enabledelayedexpansion
::java -jar ZipCenOp.jar r %1
set ZipCenOp=%cd%\ZipCenOp.jar

cd /d %~dp1

set h=%TIME: =0% && set h=!h:~0,2!
set "Ymd=%date:~0,4%%date:~5,2%%date:~8,2%%h%%time:~3,2%%time:~6,2%"
set "new_name=%~n1_%Ymd%%~x1"
set "folder=%~n1_%Ymd%"

copy "%1" "%new_name%"
java -jar %ZipCenOp% r "%new_name%"
winrar x "%new_name%" * "%folder%\"
