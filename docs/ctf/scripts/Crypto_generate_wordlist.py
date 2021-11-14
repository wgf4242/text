# https://stackoverflow.com/questions/6792803/finding-all-possible-case-permutations-in-python

def gen_possible_case1():
    def all_casings(input_string):
        if not input_string:
            yield ""
        else:
            first = input_string[:1]
            if first.lower() == first.upper():  # 非字母
                for sub_casing in all_casings(input_string[1:]):
                    yield first + sub_casing
            else:  # 字母
                for sub_casing in all_casings(input_string[1:]):
                    yield first.lower() + sub_casing
                    yield first.upper() + sub_casing

    [print(x) for x in all_casings("foo")]


def gen_possible_case2():
    import itertools

    chars = "abc"
    results = list(map(''.join, itertools.product(*zip(chars.upper(), chars.lower()))))

    print(results)


def gen_possible_case3():
    txt = 'mss2021ctf'
    strlen = len(txt)

    def fuzz(pre, i):
        if i < strlen:
            if 97 <= ord(txt[i]) <= 122:
                fuzz(pre + txt[i], i + 1)
                fuzz(pre + chr(ord(txt[i]) -32), i + 1)
            else:
                fuzz(pre + txt[i], i + 1)
        else:
            print(pre)

    fuzz('', 0)


if __name__ == '__main__':
    # gen_possible_case1()
    # gen_possible_case2()
    gen_possible_case3()
