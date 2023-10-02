; 在 gdb$ 提示符下使用
numpad8::
string1 := "python exec(open('pwn_00_02_myscript.py').read())`n"
SendByClipboard( string1)
Return

SendByClipboard( string, BackupClipBoard = false )
{
    if(BackupClipBoard)
        ClipSaved := ClipboardAll
    ClipBoard := string
    Send +{insert}
    if(BackupClipBoard)
    {
        Clipboard := ClipSaved
        ClipSaved =
    }
}
