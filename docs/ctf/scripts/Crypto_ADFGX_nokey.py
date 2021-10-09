import re


def uncipher_AFGDX(txt, key = 'phqgmeaynofdxkrcvszwbutil'):
    txt = txt.replace(' ', '').lower()
    lst = []
    for i in range(0, len(key), 5):
        lst.append(key[i:i + 5])

    groups = re.findall(r'(\w\w)', txt)
    d = {"a": 0, "d": 1, "f": 2, "g": 3, "x": 4}
    for a, b in groups:
        x, y = d[a], d[b]
        print(lst[x][y], end='')


if __name__ == '__main__':
    uncipher_AFGDX('AG DX AG DX AG DX')
