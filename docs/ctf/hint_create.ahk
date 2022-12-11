FileEncoding , UTF-8-RAW
#Include <WinClipAPI>
#Include <WinClip>
+/::send,^c
+b::
func("blockchain")
return
+c::
func("Crypto")
return
+p::
func("pwn")
return
+m::
func("Misc")
return
+r::
func("Reverse")
return
+w::
func("Web")
return
+o::  ;mobile
func("mobile")
return
+g::  ;game
func("game")
return
+i::  ;iot
func("iot")
return
]::  ; root dir
func("")
return

MD5(string, case := False)    ; by SKAN | rewritten by jNizM
{
    static MD5_DIGEST_LENGTH := 16
    hModule := DllCall("LoadLibrary", "Str", "advapi32.dll", "Ptr")
    , VarSetCapacity(MD5_CTX, 104, 0), DllCall("advapi32\MD5Init", "Ptr", &MD5_CTX)
    , DllCall("advapi32\MD5Update", "Ptr", &MD5_CTX, "AStr", string, "UInt", StrLen(string))
    , DllCall("advapi32\MD5Final", "Ptr", &MD5_CTX)
    loop % MD5_DIGEST_LENGTH
        o .= Format("{:02" (case ? "X" : "x") "}", NumGet(MD5_CTX, 87 + A_Index, "UChar"))
    return o, DllCall("FreeLibrary", "Ptr", hModule)
} ;https://autohotkey.com/boards/viewtopic.php?f=6&t=21

clean(var) {
	NewStr := RegExReplace(var, "[\(\)*^:?]" , "_")
	; 去 emoji 添加md5, emoji文件名无法上传到网盘
	if (RegExMatch(NewStr, "[\x{1F434}-\x{Fffff}]")) {
		NewStr := RegExReplace(NewStr, "[\x{1F434}-\x{Fffff}]" , "")        ; U+1F434 code for this horse
		NewStr := NewStr "_" MD5(NewStr)
	}
	return NewStr
}

func(foo) {
	global dirName

	varArray := StrSplit(Clipboard, "`r`n")
	if foo
	  dirName:= foo . "\" . clean(varArray[1])
	else 
	  dirName:= clean(varArray[1])
	FileCreateDir, %dirName%
	; FileAppend, %Clipboard%, %dirName%\hint.txt
	file := FileOpen(dirName . "\hint.txt", "w")
	file.write(Clipboard)

	links := extractLink()
	file.write(links)
	file.close()
}

^q::ExitApp


extractImages(txt, pattern:="<img[^>]+>") {
	global dirName
    result:=""
    X := True ; isFind
    while (X := RegExMatch(txt, pattern, M, X + StrLen(M))) {
        if !StrLen(M) ; M: output Match
            X++, continue
        else {
            ; msgbox % M
            result := result M "`n"
            FoundPos := RegExMatch(M, "http.*?(?="")", link)
            SplitPath, link , filename
            ; MsgBox % M "`n" link "`nfilenaame: " dirName "\" filename
            UrlDownloadToFile, %link%, %dirName%\%filename%
        }
    }
    return result
}

extractLink() {
	res:="`n`n"
	f:=Winclip.GetHTML()
	extractImages(f)

	reg=<a href="(.*?)".*?>(.*?)<
	X := True
	while (X := RegExMatch(f, reg, M, X + StrLen(M)))
	    if !StrLen(M)
	        X++, continue
	    else {
	        ; M:  href="http://xxx"
	        ; M1: http://xxx
	        ; MsgBox % M1 M2
	        res:= res M2 ": " M1 "`n"
	    }
	 ; msgbox % res
    return res
}