a = 'uozt{Zgyzhv_xlwv_uiln_xguhsld}'
import string
t1 = string.ascii_lowercase + string.ascii_uppercase
t2 = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
print(t1, t2)
trans = str.maketrans(t2, t1)

b = a.translate(trans)
print(b)