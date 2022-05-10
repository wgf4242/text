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

clean(var) {
	NewStr := RegExReplace(var, "[\(\)*^:?]" , "_")
	return NewStr
}

func(foo) {
	varArray := StrSplit(Clipboard, "`r`n")
	dirName:= foo . "\" . clean(varArray[1])
	FileCreateDir, %dirName%
	FileAppend, %Clipboard%, %dirName%\hint.txt
}

^q::ExitApp