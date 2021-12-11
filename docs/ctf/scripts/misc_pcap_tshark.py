import os
os.system(r'tshark -r ctf.pcap -T fields -e dns.qry.name|sed "/^\s*$/d" > dns.txt')
# only query no response
os.system(r'tshark -r ctf.pcap -T fields -e dns.qry.name -Y "dns && (dns.flags.response == 0) && ! dns.response_in" |sed "/^\s*$/d" > dns1.txt')

# export http
os.system(r'tshark -r ctf.pcap -T fields -e http.response.line -e media.type -Y http > http.txt')
