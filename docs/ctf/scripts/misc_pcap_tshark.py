#/usr/bin/python3
import os
# init 
os.system(r'''alias urldecode='python3 -c "import sys; from urllib.parse import unquote; print(unquote(sys.stdin.read()));"' ''')

os.system(r'tshark -r a.pcapng -T fields -e dns.qry.name|sed "/^\s*$/d" > dns.txt')
# only query no response
os.system(r'tshark -r a.pcapng -T fields -e dns.qry.name -Y "dns && (dns.flags.response == 0) && ! dns.response_in" |sed "/^\s*$/d" > dns1.txt')

# export http
os.system(r'tshark -r a.pcapng -T fields -e http.response.line -e media.type -Y http > http.txt')
os.system(r'tshark -r a.pcapng -T fields -e text -e media.type -Y http | sed "/^Timestamps[\t\s]*$/d"  > http_text.txt')
os.system(r'tshark -r a.pcapng -T fields -e http.request.full_uri -e media.type -Y http | sed "/^\s*$/d" | urldecode > http_uri.txt')
os.system(r'mkdir -p extract &&  tshark -r a.pcapng --export-objects "http,./extract/"')

# icmp
os.system(r'tshark -r a.pcapng -T fields -e data.len -Y "icmp.type == 8" > icmp.txt')

# usb
os.system(r'''tshark -r a.pcapng -T fields -e usb.capdata | sed "/^\s*$/d" > usbdata.txt''')
os.system(r'''tshark -r a.pcapng -T fields -Y 'usb.addr == "2.10.1"' -e usb.capdata | sed "/^\s*$/d" > usbdata1.txt''')
os.system(r'''tshark -r a.pcapng -T fields -Y 'usb.addr == "2.8.1"' -e usb.capdata | sed "/^\s*$/d" > usbdata2.txt''')
