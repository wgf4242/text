# IDAPython： Generating disassembly lines and instruction decoding [qRS6310gDoQ].mkv

idc.GetDisasm(idc.here())
# ida 控制台
?idaapi.generate_disasm_line
idaapi.generate_disasm_line(idc.here(), 0) # '\x01\x05call\x02\x05    \x01)\x01%\x01(00007FF6FF1F9DE0puts\x02%\x02)'
s = idaapi.generate_disasm_line(idc.here(), 0)
idaapi.tag_remove(s) # 'call    puts'

s = idc.GetDisasm(idc.here())
s.split(' ')         # ['call', '', '', '', 'puts']
idc.print_insn_mnem(here()) # 'call'
idc.print_operand(idc.here(), 0) # 'puts'

IDC> decode_insn(here)
"%d" % idaapi.NN_mov



import idautils
import idc
import idaapi

ea = idaapi.get_screen_ea() # idc.here()

inst = idautils.DecodeInstruction(ea)
print(inst[0].reg)
if inst:

    if inst[0].reg == 7:
        print("Found EDI = 7")
    # idautils.procregs.Rsp
    # idautils.procregs.R8
    # if inst[0] == idautils.procregs.R8:
    #     print("Found EDI use!")
