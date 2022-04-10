# 先 key=-5 和 NSSCTF 对比为先差数列
# 再 Get Flag

import string


class Caesar:
    def __init__(self, txt) -> None:
        self.txt = txt

    def do_base(self, asc, char, offset, base=26):
        asc = ord(asc)
        result = (ord(char) - asc + offset) % base + asc
        return chr(result)

    def do_upper_letters(self, char, offset):
        return self.do_base('A', char, offset)

    def do_lower_letters(self, char, offset):
        return self.do_base('a', char, offset)

    def do_digit(self, char, offset):
        return self.do_base('0', char, offset, 10)

    def get_it(self, offset):
        lst = []
        for c in self.txt:
            lst.append(self.get_char_caesar(c, offset))
        return ''.join(lst)

    def get_char_caesar(self, c, offset):
        if c in string.ascii_uppercase:
            return self.do_upper_letters(c, offset)
        elif c in string.ascii_lowercase:
            return self.do_lower_letters(c, offset)
        elif c in string.digits:
            return self.do_digit(c, offset)
        else:
            return c

    def get_increment_caesar(self, txt, offset):
        lst = []
        for i, c in enumerate(txt):
            caesar_char = self.get_char_caesar(c, offset)
            box = chr(ord(caesar_char) + offset + i)
            lst.append(box)
        return ''.join(lst)

    def get_increment(self, txt, offset):
        lst = []
        for i, c in enumerate(txt):
            box = chr(ord(c) + offset + i)
            lst.append(box)
        return ''.join(lst)


if __name__ == '__main__':
    c = r'NRQ;P<uLliW^(XQ/QT\NDh'
    enc_obj = Caesar(c)
    caesar_key_5 = enc_obj.get_it(-5)
    inc_5 = enc_obj.get_increment(caesar_key_5, 5)

    print(caesar_key_5)
    print(inc_5)
