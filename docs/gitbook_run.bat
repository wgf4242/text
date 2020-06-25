 rem @Echo off
 rem :Start
 rem call gitbook serve
 rem goto Start

rd /s /q _book
start "" cmd.exe /k "timeout /t 1 && rd /s /q _book"
call gitbook serve
rd /s /q _book
