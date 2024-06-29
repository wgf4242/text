import re
def waf(string):
    string=str(string)
    pattern = "os|timeit|platform|subprocess|pty|commands"
    pattern +="|file|open|codecs|fileinput"
    pattern +="|exec|eval|execfile|compile"
    pattern +="|\.\.|http:"
    pattern +="|request|url_for|get_flashed_messages|lipsum|\{|set|dict|\_|\[|pop|getitem|class"
    pattern +="|script"
    pattern +="select|update|\'|\%"
    matches = re.findall(pattern, string)
    if matches:
        return True
    return False

# 调用
if waf(args):
    return "no"
