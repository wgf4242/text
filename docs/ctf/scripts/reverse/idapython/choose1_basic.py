import idaapi

class MyChoose(idaapi.Choose):
    def __init__(self, title, /, flags=0, embedded=False, width=None, height=None):
        super().__init__(
            title,
            [
                ["Address", 10],
                ["Name", 30],
                ["Type", 8]
            ],
            flags=flags | idaapi.Choose.CH_RESTORE,
            embedded=embedded,
            width=width,
            height=height
        )

    def OnGetSize(self):
        return 10

    def OnGetLine(self, n):
        return [("%x" % (0x401000 + n*10)), ("Name %d" % n), ("Type %d" % n)]

if __name__ == '__main__':
    c = MyChoose("Chooser test")
    c.Show(modal=False)