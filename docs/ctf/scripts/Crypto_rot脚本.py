# -*- coding: utf-8 -*-             <--------入手点
def rot(s,OffsetX):
    def _rot(ch):
        try:
            asc = ord(ch)
        except:
            return ch
        if (asc > 96) and (asc < 123):
            return chr((asc-97+OffsetX).__mod__(26) + 97)
        elif (asc > 64) and (asc < 91):
            return chr((asc-65+OffsetX).__mod__(26) + 65)
        else:
            return ch

    return ''.join([_rot( c ) for c in s])