import idaapi


class MyChoose(idaapi.Choose):
    def __init__(self, title, /, n=12, flags=0, embedded=False, width=None, height=None):
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
        self.popup_names = ["Inzert", "Del leet", "Ehdeet", "Ree fresh"]
        self.data = [
            [("%x" % (0x401000 + n * 10)), ("Name %d" % n), ("Type %d" % n)]
        ]

    def OnGetSize(self):
        return len(self.data)

    def OnGetLine(self, n):
        return self.data[n]

    def OnGetIcon(self, n):
        return n + 1

    def OnGetLineAttr(self, n):
        if n < 10:
            if n % 2 == 0:
                return [0xFF0000, idaapi.CHITEM_BOLD]
            else:
                return [0x0000FF, idaapi.CHITEM_ITALIC]
        return (0xffffff, 0)

    def OnDeleteLine(self, sel):
        """
        User deleted an element
        :param sel: the current selection
        :return: a tuple (changed, selection)
        """
        del self.data[sel]
        print("OnDeleteLine: sel=%d" % sel)
        return [idaapi.Choose.ALL_CHANGED] + self.adjust_last_item(sel)


if __name__ == '__main__':
    c = MyChoose("Chooser test")
    # c.Show(modal=False)
    r = c.Show(modal=True)
    print("dialog returned=%d" % r)
