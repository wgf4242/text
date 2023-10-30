#requires AutoHotkey v2.0

Numpad7::
{
  ; TC copy filenames 后按7
  TestString := A_Clipboard
  global v :=1
  global ar := StrSplit(TestString, "`r`n")
}

Numpad8::
{
  if FileExist("a.bat")
    FileRecycle "a.bat"
  ; TC copy target full paths 后按8
  ; msgbox ar[1]
  paths := A_Clipboard
  targets := StrSplit(paths, "`r`n")
  For index, color in ar
    {
    ; MsgBox Format("move `"{1}`" `"{2}`" ", ar[index] ,targets[index])
    line := Format("move `"{1}`" `"{2}`" ", ar[index] ,targets[index])
    FileAppend line "`r`n", "a.bat"
  }
  ; MsgBox Format("{2:x}{1:02x}", arr*)
}

^q::ExitApp