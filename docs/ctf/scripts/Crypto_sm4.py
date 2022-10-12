from Crypto.Cipher import ARC4
from sm4 import SM4Key

c = bytes.fromhex('cc53de43058c79e4e13dbfe4e1ece82ec7d70b0fe460d50a6e2dfbbdac0b22173124ac7dee560b026b9b4cf1394c9493ad62874b4ef2125bbe27f99827d2a801b1b994c90bc31caea1cc9dc09362b518')
key = b'd0cac74c1bbeea071817360e491585e8'
cipher = ARC4.new(key)
m = cipher.decrypt(c)
key0 = SM4Key(b'xc08asb890ajds0a')
print(key0.decrypt(m))
