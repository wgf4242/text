; 设置文件路径
FilePath := "out.txt"
FileContent := ""
BlockLength := 3700
CurrentIndex := 1

; 读取文件内容
FileRead, FileContent, %FilePath%

; 按下 Ctrl+] 时运行函数 'SendContentBlock'
^]::
    loop,{
    SendContentBlock(FileContent, BlockLength, CurrentIndex)

    }
    return

SendContentBlock(FileContent, BlockLength, ByRef CurrentIndex) {
    ; 提取 5000 字符的块
    ContentBlock := SubStr(FileContent, CurrentIndex, BlockLength)
    
    ; 如果内容不为空，则发送到剪贴板并通过 Ctrl+V 粘贴
    if (ContentBlock != "") {
        ; 将内容发送到剪贴板
        Clipboard := "echo " ContentBlock ">>out`n"
        ClipWait

        ; 模拟按下和松开 Ctrl+V
        Send, ^v{enter}
        sleep 5

        ; 更新索引以便下次按键读取下一块
        CurrentIndex += BlockLength
    }
    else {
        MsgBox, No more content to send
        send, certutil.exe -decode .\out artifact.exe
        ExitApp, 0
    }
}

^q:: ExitApp, 0