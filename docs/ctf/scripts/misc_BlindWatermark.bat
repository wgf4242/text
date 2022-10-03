@echo off
::1.claunch parameter 添加tool_path 路径到参数 如 F:\downloads\@CTF
::2.拖拽文件到claunch的图标
set cur=%cd%
set tool_path=%1
set file=%2
:: set parent in call below
call :check_symbol %2
start "" %tool_path%\盲水印imagein\imageIN_Beta1.0.exe
start "" %tool_path%\Misc_BlindWatermark_隐形水印工具.exe
::


cd /d %parent%
copy "%cur%\misc_blindWaterMark盲水印_bwmforpy3.py" bwmforpy3.py
copy "%cur%\misc_blindWaterMark盲水印_pinyubwm.py" pinyubwm.py
java -jar %tool_path%\Misc_BlindWatermark.jar decode -c "%file%" output.jpg
pause
goto :EOF

:check_symbol
set parent=%~dp1
echo parent is %parent%
goto :EOF
