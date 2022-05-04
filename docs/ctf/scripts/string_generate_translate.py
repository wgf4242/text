def generate(n=18):
    result = ""
    for i in range(n):
        s = chr(i + 0x31)
        result += s
    print(result)
    return result


def get_trans_table(a, b):
    lst = []
    for i in range(len(a)):
        origin = i
        c = a[i]
        after = b.index(c)
        lst.append((origin, after))
    return lst


def translate_by_index(tab, value):
    f = ''
    for i_origin, i_after in tab:
        f += value[i_after]
    return f


if __name__ == '__main__':
    da = "123456789:;<=>?"
    db = "=>?789:;<123456"
    tab = get_trans_table(da, db)
    print(tab)
    plain = translate_by_index(tab, db)
    print(plain)
