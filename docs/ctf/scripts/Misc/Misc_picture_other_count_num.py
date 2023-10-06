from PIL import Image

img = Image.open('solved.bmp')
w, h = img.size
count = []
for i in range(h):
    tmp = 0
    for j in range(w):
        pixel = img.getpixel((j, i))
        if pixel != (0, 0, 0):
            tmp += 1
    if tmp != 10:
        count.append(tmp - 10)
print(count)
print(''.join([chr(i) for i in count]))
