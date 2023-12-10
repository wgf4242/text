# https://blog.csdn.net/qq_45628145/article/details/106358102
import string
from collections import OrderedDict


class FourSquare:

    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
        table = string.ascii_lowercase.replace('q', '')

        self.key1 = self.uniq(key1 + table)
        self.key2 = self.uniq(key2 + table)

    def uniq(self, string):
        ordered_dict = OrderedDict.fromkeys(string)
        result = ''.join(ordered_dict.keys())
        return result

    def decode(self, cipher):
        return


if __name__ == '__main__':
    key1 = 'information'
    key2 = 'engineering'

    fs = FourSquare(key1, key2)
    res = fs.decode('zhnjinhoopcfcuktlj')
    assert res == 'youngandsuccessful'
