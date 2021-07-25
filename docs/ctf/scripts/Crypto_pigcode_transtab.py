txt= "ocjp{zkirjwmo-ollj-nmlw-joxi-tmolnrnotvms}"

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "jklmnopqrabcdefghiwxyzstuv"
trantab = str.maketrans(intab, outtab)
print(txt.translate(trantab))
