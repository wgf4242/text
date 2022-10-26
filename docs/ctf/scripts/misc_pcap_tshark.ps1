# init
tshark -r a.pcapng -T fields -e dns.qry.name | where { $_.trim() }> dns.txt
mkdir tcp_export 2> nul
# only query no response
tshark -r a.pcapng -T fields -e dns.qry.name -Y "dns && (dns.flags.response == 0) && ! dns.response_in" | where { $_.trim() }> dns1.txt

# export http
tshark -r a.pcapng -T fields -e http.response.line -e media.type -Y http> http.txt
tshark -r a.pcapng -T fields -e text -e media.type -Y http | sed "/^Timestamps[\t\s]*$/d" > http_text.txt
tshark -r a.pcapng -T fields -e http.request.full_uri -e media.type -Y http | where { $_.trim() }> http_uri.txt
mkdir -p extract &&  tshark -r a.pcapng --export-objects "http,./extract/" 1> nul

# icmp
tshark -r a.pcapng -T fields -e data.len -Y "icmp.type == 8"> icmp.txt

# usb
tshark -r a.pcapng -T fields -e usb.capdata | where { $_.trim() }> usbdata.txt
tshark -r a.pcapng -T fields -Y 'usb.addr == "2.10.1"' -e usb.capdata | where { $_.trim() }> usbdata1.txt
tshark -r a.pcapng -T fields -Y 'usb.addr == "2.8.1"' -e usb.capdata | where { $_.trim() }> usbdata2.txt
## 数位板
tshark -r a.pcapng -T fields -e usbhid.data -Y "usb.device_address == 2.6.1"> usbdata3_shuweiban.txt

# tcp
# find . -size 0 -print -delete
# PCAP="a.pcapng";total_streams=$(tshark -r $PCAP -Y "tcp" -T fields -e tcp.stream | sort -u | wc -l); total_streams=$(($total_streams - 1)); for i in $(seq 0 $total_streams); do tshark -r $PCAP -Y "tcp.stream eq $i" -T fields -e tcp.payload | xxd -r> stream$i-raw.out; done

# clean
Get-ChildItem -Path "." -Recurse | where { $_.Length -eq 0 } | Remove-Item

# tshark examples
# https://mymanfile.com/?p=1973