import struct


def bytes_to_4lst(a: list) -> list:
    b = bytes(a)
    lst = []
    for i in range(0, len(b), 4):
        unpack = struct.unpack('<I', b[i: i + 4])[0]
        # print(i_)
        lst.append(unpack)
    return lst


if __name__ == '__main__':
    a = [20, 105, 41, 173, 62, 178, 75, 159, 182, 170, 33, 91, 46, 230, 57, 64, 234, 134, 33, 151, 82, 198, 52, 227]
    o = bytes_to_4lst(a)
    print(o)
