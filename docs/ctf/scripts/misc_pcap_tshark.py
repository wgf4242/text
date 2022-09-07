import os
os.system(r'tshark -r a.pcapng -T fields -e dns.qry.name|sed "/^\s*$/d" > dns.txt')
# only query no response
os.system(r'tshark -r a.pcapng -T fields -e dns.qry.name -Y "dns && (dns.flags.response == 0) && ! dns.response_in" |sed "/^\s*$/d" > dns1.txt')

# export http
os.system(r'tshark -r a.pcapng -T fields -e http.response.line -e media.type -Y http > http.txt')
os.system(r'mkdir -p out &&  tshark -r a.pcapng --export-objects "http,./out/"')

# icmp
os.system(r'tshark -r a.pcapng -T fields -e data.len -Y "icmp.type == 8" > icmp.txt')

# usb
os.system(r'''tshark -r a.pcapng -T fields -e usb.capdata | sed "/^\s*$/d" > usbdata.txt''')
os.system(r'''tshark -r a.pcapng -T fields -Y 'usb.addr == "2.10.1"' -e usb.capdata | sed "/^\s*$/d" > usbdata1.txt''')
os.system(r'''tshark -r a.pcapng -T fields -Y 'usb.addr == "2.8.1"' -e usb.capdata | sed "/^\s*$/d" > usbdata2.txt''')
