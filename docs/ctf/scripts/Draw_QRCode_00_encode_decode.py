def generate_qrcode(txt, output):
    import pyqrcode
    qr = pyqrcode.create(txt)
    qr.png(output, scale=6)


def decode_qrcode(file):
    from PIL import Image
    from pyzbar.pyzbar import decode
    data = decode(Image.open(file))
    print(data)
    print(data[0].data)


if __name__ == '__main__':
    txt = "HORN O.K. PLEASE."
    filename = "horn.png"
    
    generate_qrcode(txt, filename)
