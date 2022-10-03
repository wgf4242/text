#/usr/bin/python3
import os
# init 

os.system(r'tshark -r a.pcapng -T fields -e dns.qry.name|sed "/^\s*$/d" > dns.txt')
os.system(r'mkdir tcp_export 2>/dev/null')
# only query no response
os.system(r'tshark -r a.pcapng -T fields -e dns.qry.name -Y "dns && (dns.flags.response == 0) && ! dns.response_in" |sed "/^\s*$/d" > dns1.txt')

# export http
os.system(r'tshark -r a.pcapng -T fields -e http.response.line -e media.type -Y http > http.txt')
os.system(r'tshark -r a.pcapng -T fields -e text -e media.type -Y http | sed "/^Timestamps[\t\s]*$/d"  > http_text.txt')
urldecode = 'python3 -c "import sys; from urllib.parse import unquote; print(unquote(sys.stdin.read()));"'
os.system(rf'tshark -r a.pcapng -T fields -e http.request.full_uri -e media.type -Y http | sed "/^\s*$/d" | {urldecode} > http_uri.txt')
#os.system(r'''alias urldecode='python3 -c "import sys; from urllib.parse import unquote; print(unquote(sys.stdin.read()));"' ''')
#os.system(r'tshark -r a.pcapng -T fields -e http.request.full_uri -e media.type -Y http | sed "/^\s*$/d" | urldecode > http_uri.txt')
os.system(r'mkdir -p extract &&  tshark -r a.pcapng --export-objects "http,./extract/" 1>/dev/null')

# icmp
os.system(r'tshark -r a.pcapng -T fields -e data.len -Y "icmp.type == 8" > icmp.txt')

# usb
os.system(r'''tshark -r a.pcapng -T fields -e usb.capdata | sed "/^\s*$/d" > usbdata.txt''')
os.system(r'''tshark -r a.pcapng -T fields -Y 'usb.addr == "2.10.1"' -e usb.capdata | sed "/^\s*$/d" > usbdata1.txt''')
os.system(r'''tshark -r a.pcapng -T fields -Y 'usb.addr == "2.8.1"' -e usb.capdata | sed "/^\s*$/d" > usbdata2.txt''')
## 数位板
os.system(r'''tshark -r a.pcapng -T fields -e usbhid.data -Y "usb.device_address == 2.6.1"> usbdata3_shuweiban.txt''')

# tcp
os.system(r'''find . -size 0 -print -delete''')
os.system(r'PCAP="a.pcapng";total_streams=$(tshark -r $PCAP -Y "tcp" -T fields -e tcp.stream | sort -u | wc -l); total_streams=$(($total_streams - 1)); for i in $(seq 0 $total_streams); do tshark -r $PCAP -Y "tcp.stream eq $i" -T fields -e tcp.payload | xxd -r > stream$i-raw.out; done')


# clean
os.system(r'''find . -size 0 -print -delete''')

# tshark examples
# https://mymanfile.com/?p=1973