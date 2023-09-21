import unittest
import idaapi


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_print_names(self):
        # 和 name 窗口相同
        import idautils

        for ea, name in idautils.Names():
            print(f"{ea:x} {name}")

    def test_register(self):
        import idautils
        print(f"the value of EAX is {idautils.cpu.eax}")
        idautils.cpu.eax = 15

    def test_msg(self):
        # 不用额外引入
        idaapi.msg("Hello\n")

