def test_ror5():

    def ror5(x, i):
        """
        Rotate right x[0:5] by i position
        https://www.bilibili.com/video/BV1UU4y1T7X8?p=17
        """
        return ((x >> i) | (x << (5 - i))) & 0x1f  # 00011111b

    assert ror5(0x1f, 1) == 0x1f
    assert ror5(0x10, 1) == 0x08
    assert ror5(0x08, 1) == 0x04
    assert ror5(0x10, 3) == 0x02
    assert ror5(0x1, 1) == 0x10
    if __name__ == "__main__":
        r = ror5(0x1f, 1)
        print(bin(r))
if __name__ == '__main__':
    test_ror5()