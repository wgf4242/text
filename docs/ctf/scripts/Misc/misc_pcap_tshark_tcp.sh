# 每个流提取出一个cap
for stream in `tshark -r file2.pcap -T fields -e tcp.stream | sort -n | uniq | tr -d '\r'`
do
    tshark -r file2.pcap -w res-$stream.cap -2 -R "tcp.stream==$stream"
    # tshark -r file2.pcap -w stream-$stream.cap -Y "tcp.stream==$stream"
done