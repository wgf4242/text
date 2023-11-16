import lief
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_basic(self):
        # 读取二进制文件
        binary = lief.parse("shift_f7")

        # 过滤掉低于0x1000地址的段和.dynamic段
        filtered_sections = [section for section in binary.sections if section.virtual_address >= 0x1000 and section.name != '.dynamic']

        # 按地址从低到高排序
        sorted_sections = sorted(filtered_sections, key=lambda section: section.virtual_address)

        # 输出排序后的段名和地址
        for section in sorted_sections:
            print(section.name, end='')
        # flag{You_ar3_g0od_at_f1nding_ELF_segments_name}

    def test_common(self):
        binary = lief.parse("shift_f7")
        # header
        header = binary.header
        hex(header.entrypoint)
        header.entrypoint = 0x123
        binary.write("ls.modified")

    def test_sections(self):
        for section in binary.sections:
            print(section.name)  # section's name
            print(section.size)  # section's size
            print(len(section.content))  # Should match the previous print

    def test_win_pe(self):
        import lief
        binary = lief.parse("C:\\Windows\\explorer.exe")

        print(binary.dos_header)
        print(binary.header)
        print(binary.optional_header)

        # imported functions
        ## Using the abstract layer
        for func in binary.imported_functions:
            print(func)

        ## Using the PE definition
        for func in binary.imports:
            print(func)


        for imported_library in binary.imports:
            print("Library name: " + imported_library.name)
            for func in imported_library.entries:
                if not func.is_ordinal:
                    print(func.name)
                print(func.iat_address)
