from PIL import Image
def generateKeyofEncrypt(a,b):
    return [[1,a],[b,a*b+1]]
def generateKeyofDencrypt(a,b):
    return [[a*b+1,-a],[-b,1]]
def arnold(img,key):
    width = img.size[0]
    height = img.size[1]
    res = Image.new("RGB",img.size)
    for y in range(height):
        for x in range(width):
            color = img.getpixel((x,y))
            x_new = (key[0][0]*x+key[0][1]*y)%width
            y_new = (key[1][0]*x+key[1][1]*y)%height
            res.putpixel((x_new,y_new),color)
    return res
def main():
    a,b=20,22
    img = Image.open("flag.bmp")
    key_encrypt = generateKeyofEncrypt(a,b)
    key_dencrypt = generateKeyofDencrypt(a,b)
    arnold(img,key_dencrypt).show()
main()
