# pip install python-snap7
import snap7

# 创建一个客户端对象
client = snap7.client.Client()

# 连接到PLC
client.connect('192.168.80.133', 0, 1)
# data = client.read_area(snap7.types.Areas.MK, 1, 0, 1)
# print(data)

# 写入数据 M0.0
client.write_area(snap7.types.Areas.MK, 0, 0, b'\x01')
# client.write_area(snap7.types.Areas.MK, 0, 0,  bytearray([0b00000001]))
# data = client.read_area(snap7.types.Areas.MK, 0, 0, 1)
# print(data)


# client.disconnect()
