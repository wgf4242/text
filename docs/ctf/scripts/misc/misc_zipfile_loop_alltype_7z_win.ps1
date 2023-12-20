# 太慢了用 python脚本跑吧
# 自动用文件名作为密码进行解压
$file = (Get-ChildItem *.zip)[0]
$cur = (Get-Location).Path
Write-Host $file
$counter = 0

while (1) {
  # $cmd = "7z -y x $($file) -o$($cur+"\"+$counter)"
  $cmd = "7z -y x $($file) -p$($file.baseName) -o$($cur+"\"+$counter)"

  Write-Host $cmd
  Invoke-Expression $cmd

  $list = Get-ChildItem $("$counter"+"/*.zip")
  if ($list.Length -eq 0) { exit }

  $file = $list[0]
  $counter++
  Write-Host $file.name
}