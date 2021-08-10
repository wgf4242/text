s = "MMDDMDMDMMMDDDMDMDDMMMMMMMDDMDMMDDM"


def method1(g):
    data = ''.join(list(g))
    trans1 = 'AB'
    trans2 = 'BA'
    tab1 = str.maketrans('' + data, trans1)
    tab2 = str.maketrans('' + data, trans2)
    res1 = s.translate(tab1)
    res2 = s.translate(tab2)

    print()
    dir1 = {'aaaaa': 'A', 'aaaab': 'B', 'aaaba': 'C', 'aaabb': 'D', 'aabaa': 'E', 'aabab': 'F', 'aabba': 'G', 'aabbb': 'H', 'abaaa': 'I',
            'abaab': 'J', 'ababa': 'K', 'ababb': 'L', 'abbaa': 'M', 'abbab': 'N', 'abbba': 'O', 'abbbb': 'P', 'baaaa': 'Q', 'baaab': 'R',
            'baaba': 'S', 'baabb': 'T', 'babaa': 'U', 'babab': 'V', 'babba': 'W', 'babbb': 'X', 'bbaaa': 'Y', 'bbaab': 'Z'}
    dir2 = {'AAAAA': 'a', 'AABBA': 'g', 'ABBAA': 'n', 'BAABA': 't', 'AAAAB': 'b', 'AABBB': 'h', 'ABBAB': 'o', 'BAABB': 'u/v',
            'AAABA': 'c', 'ABAAA': 'i/j', 'ABBBA': 'p', 'BABAA': 'w', 'AAABB': 'd', 'ABAAB': 'k', 'ABBBB': 'q', 'BABAB': 'x',
            'AABAA': 'e', 'ABABA': 'l', 'BAAAA': 'r', 'BABBA': 'y', 'AABAB': 'f', 'ABABB': 'm', 'BAAAB': 's', 'BABBB': 'z'}
    bacon_table1(dir1, res1)
    bacon_table2(dir2, res2)


def bacon_table2(dir2, res2):
    try:
        print(res2)
        flag2 = ""
        for i in range(0, len(res2), 5):
            cur2 = res2[i:i + 5]
            flag2 += dir2[cur2.lower()]
        print(flag2)
    except Exception as e:
        print('2 error', e)


def bacon_table1(dir1, res1):
    try:
        print(res1)
        flag1 = ""
        for i in range(0, len(res1), 5):
            cur1 = res1[i:i + 5]
            flag1 += dir1[cur1.lower()]
        print(flag1)
    except Exception as e:
        print('1 error', e)


if __name__ == "__main__":
    g = sorted(set(s), key=lambda x: ord(x))
    method1(g)
    g = g[::-1]
    method1(g)
