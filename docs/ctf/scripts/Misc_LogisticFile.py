import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def logic_encrypt(im, x0, mu):
    xsize, ysize = im.shape
    # print(xsize, ysize)
    im = np.array(im).flatten()
    num = len(im)
    
    for i in range(100):
        x0 = mu * x0 * (1-x0)
        
    E = np.zeros(num)
    E[0] = x0
    for i in range(0,num-1):
        E[i+1] = mu * E[i]* (1-E[i])
    E = np.round(E*255).astype(np.uint8)

    im = np.bitwise_xor(E,im)
    im = im.reshape(xsize,ysize,-1)
    im = np.squeeze(im)
    im = Image.fromarray(im)
    
    return im

img = cv2.imread('fff.jpeg',0)
img = logic_encrypt(img,0.35,3)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
s = np.log(np.abs(fshift))

plt.imshow(s,'gray')
plt.imsave("logic_encrypt.png",s)
plt.show()