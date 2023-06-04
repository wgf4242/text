import os

file = """a.pcapng"""
os.system("""tshark -r %s -Y modbus -T fields -e modbus.data |sed '/^$/d' > out""" % file)
