# [『CTF』一次曲折的流量分析](https://mp.weixin.qq.com/s/Xe-JoLSgJ7prKQcfM9RXSA)

import hashlib
import binascii
import hmac
from Crypto.Hash import MD4

# 生成 NTLM 哈希
md4_hasher = MD4.new()
md4_hasher.update("QUICAUTH-CCC123!@#".encode("utf-16-le"))
_ntlm = md4_hasher.digest()
ntlm = binascii.hexlify(_ntlm).decode('utf-8')

# 将服务器名称编码为十六进制
server = "adminSecretServer".upper().encode("utf-16-le")
server_hex = binascii.hexlify(server).decode('utf-8')

# 生成第一个 HMAC
firstHMAC = hmac.new(binascii.unhexlify(ntlm), binascii.unhexlify(server_hex), hashlib.md5).hexdigest()

# type2Challange
type2Challange = "d158262017948de9010100000000000058b2da67cbe0d001c575cfa48d38bec50000000002001600450047004900540049004d002d00500043003100340001001600450047004900540049004d002d00500043003100340004001600650067006900740069006d002d00500043003100340003001600650067006900740069006d002d0050004300310034000700080058b2da67cbe0d0010600040002000000080030003000000000000000000000000030000065d85a4000a167cdbbf6eff657941f52bc9ee2745e11f10c61bb24db541165800a001000000000000000000000000000000000000900240063006900660073002f003100390032002e003100360038002e0031002e00310030003700000000000000000000000000"

# 生成 NTLMv2 响应
ntlmv2 = hmac.new(binascii.unhexlify(firstHMAC), binascii.unhexlify(type2Challange), hashlib.md5).hexdigest()
print(ntlmv2)