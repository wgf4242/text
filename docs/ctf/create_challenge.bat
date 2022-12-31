md @Challenge
cd @Challenge
md Crypto
md Misc
md Web
md Reverse
md pwn
copy ..\hint_create.ahk .\

echo $ar = "copper_crown.png,silver_crown.png,gold_crown.png" -split ","^ >> clean.ps1
echo Get-ChildItem -Path "." -Recurse ^| where { $ar.Contains($_.name) } ^| Remove-Item >> clean.ps1
