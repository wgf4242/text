import base64

def get_base64_diff_value(s1, s2):
    base64chars = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    res = 0
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            return abs(base64chars.index(s1[i]) - base64chars.index(s2[i]))
            # return abs(base64chars.index(chr(s1[i])) - base64chars.index(chr(s2[i])))
    return res


def solve_stego():
    with open('2.txt', 'rb') as f:
        file_lines = f.readlines()
        bin_str = ''
        for line in file_lines:
            nline = line.replace(b'\n', b'')
            steg_line = nline
            norm_line = base64.b64encode(base64.b64decode(nline)).replace(b'\n', b'')
            # norm_line = nline.decode('base64').encode('base64').replace('\n', '')
            diff = get_base64_diff_value(steg_line, norm_line)
            pads_num = steg_line.count(b'=')
            if diff:
                bin_str += bin(diff)[2:].zfill(pads_num * 2)
            else:
                bin_str += '0' * pads_num * 2
            res_str = ''
            for i in range(0, len(bin_str), 8):
                res_str += chr(int(bin_str[i:i + 8], 2))
                print(res_str)


solve_stego()
