lstr="""U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7YSH]*=93dVZ3^S8*$:8"&:9U]RH;g=8Y!U92'=j*$KH]ZSj&[S#!gU#*dK9\."""

for p in range(127):
	str1 = ''
	for i in lstr:
		temp = chr((ord(i)+p)%127)
		if 32<ord(temp)<127 : #2
			str1 = str1 + temp
			feel = 1
		else:
			feel = 0
			break
	if feel == 1:
		print (str1)
