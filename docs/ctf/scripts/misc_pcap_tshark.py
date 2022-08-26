import os
os.system(r'tshark -r a.pcapng -T fields -e dns.qry.name|sed "/^\s*$/d" > dns.txt')
# only query no response
os.system(r'tshark -r a.pcapng -T fields -e dns.qry.name -Y "dns && (dns.flags.response == 0) && ! dns.response_in" |sed "/^\s*$/d" > dns1.txt')

# export http
os.system(r'tshark -r a.pcapng -T fields -e http.response.line -e media.type -Y http > http.txt')
os.system(r'mkdir -p out &&  tshark -r a.pcapng --export-objects "http,./out/"')

# icmp
os.system(r'tshark -r a.pcapng -T fields -e data.len -Y "icmp.type == 8" > icmp.txt')
