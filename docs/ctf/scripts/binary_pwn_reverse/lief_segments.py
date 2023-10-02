import lief

# 读取二进制文件
binary = lief.parse("shift_f7")

# 过滤掉低于0x1000地址的段和.dynamic段
filtered_sections = [section for section in binary.sections if section.virtual_address >= 0x1000 and section.name != '.dynamic']

# 按地址从低到高排序
sorted_sections = sorted(filtered_sections, key=lambda section: section.virtual_address)

# 输出排序后的段名和地址
for section in sorted_sections:
   print(section.name,end='')
#flag{You_ar3_g0od_at_f1nding_ELF_segments_name}