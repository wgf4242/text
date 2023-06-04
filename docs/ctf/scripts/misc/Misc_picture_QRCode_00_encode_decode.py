def generate_qrcode(txt, output):
    import pyqrcode
    qr = pyqrcode.create(txt)
    qr.png(output, scale=6)


def decode_qrcode(file):
    from PIL import Image
    from pyzbar.pyzbar import decode
    data = decode(Image.open(file))
    print(data)
    if data:
        print(data[0].data)
        return data[0].data
    else:
        print(f'{file} no data')


def decode_qrcode2(file):
    import cv2

    qrcode_filename = file
    qrcode_image = cv2.imread(qrcode_filename)
    qrCodeDetector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = qrCodeDetector.detectAndDecode(qrcode_image)

    print(data)


if __name__ == '__main__':
    txt = "HORN O.K. PLEASE."
    filename = "horn.png"
    
    # generate_qrcode(txt, filename)
    decode_qrcode2(filename)
