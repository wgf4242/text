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

clean(var) {
	NewStr := RegExReplace(var, "[\(\)*^:?]" , "_")
	return NewStr
}

func(foo) {

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


extractLink() {
	res:="`n`n"
	f:=Winclip.GetHTML()

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