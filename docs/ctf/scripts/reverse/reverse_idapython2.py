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

        def read_reg(name):
            rv = idaapi.regval_t()
            idaapi.get_reg_val(name, rv)
            if 'mm' in name:
                print(''.join(f'{x:X}' for x in rv.bytes()))
                # return (struct.unpack('Q',rv.bytes())[0])
                return rv.bytes()
            return rv.ival

        read_reg("xmm2")

    def test_msg(self):
        # 不用额外引入
        idaapi.msg("Hello\n")

    def test_memory(self):
        # 1. 调试内存操作
        # idc.read_dbg_byte(addr)
        # idc.read_dbg_memory(addr, size)
        # idc.read_dbg_dword(addr)
        # idc.read_dbg_qword(addr)
        # idc.patch_dbg_byte(addr, val)

        def patch_dbg_men(addr, data):
            for i in range(len(data)):
                idc.patch_dbg_byte(addr + i, data[i])

        def read_dbg_mem(addr, size):
            dd = []
            for i in range(size):
                dd.append(idc.read_dbg_byte(addr + i))
            return bytes(dd)

        # 2.本地内存操作（会修改idb数据库）
        # 静态分析时使用，会影响修改本地的静态内存，在[Patch list]窗口可以看到我们的修改
        # idc.get_qword(addr)
        # idc.patch_qword(addr, val)
        # idc.patch_dword(addr, val)
        # idc.patch_word(addr, val)
        # idc.patch_byte(addr, val)
        # idc.get_db_byte(addr)
        # idc.get_bytes(addr, size)

        # 反汇编操作
        # GetDisasm(addr) # 获取反汇编文本
        # idc.next_head(ea) # 获取下一条指令地址

        # 交叉引用分析
        for ref in idautils.XrefsTo(ea):
            print(hex(ref.frm))

    def test_ovllvm(self):
        # ollvm批量断点设置

        fn = 0x123456  # main函数的地址
        ollvm_tail = 0x567890  # ollvm 真实块的汇集点
        f_blocks = idaapi.FlowChart(idaapi.get_func(fn), flags=idaapi.FC_PREDS)
        for block in f_blocks:
            for succ in block.succs():
                if succ.start_ea == ollvm_tail:
                    print(hex(block.start_ea))
                    idc.add_bpt(block.start_ea)

        # 还可以使用 IDA 的[Breakpoint list]来批量管理，支持将需要的断点放进文件夹，还可以对文件夹的断点进行disable来暂时禁用断点
