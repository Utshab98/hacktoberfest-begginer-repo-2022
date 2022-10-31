from PIL import Image
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

im = Image.open("dexter.png", "r")
imOr = Image.open("dexter.png","r")
arr = im.load() #pixel data stored in this 2D array

def rot(A, n, x1, y1): #this is the function which rotates a given block
    temple = []
    for i in range(n):
        temple.append([])
        for j in range(n):
            temple[i].append(arr[x1+i, y1+j])
    for i in range(n):
        for j in range(n):
            arr[x1+i,y1+j] = temple[n-1-i][n-1-j]


xres = im.width
yres = im.height
BLKSZ = 50
#blocksize

for i in range(2, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(i)))):
        for k in range(int(math.floor(float(yres)/float(i)))):
            rot(arr, i, j*i, k*i)
            
for i in range(3, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(BLKSZ+2-i)))):
        for k in range(int(math.floor(float(yres)/float(BLKSZ+2-i)))):
            rot(arr, BLKSZ+2-i, j*(BLKSZ+2-i), k*(BLKSZ+2-i))

im.save("imageNew "+str(BLKSZ)+".png")
print(type(arr))
imgShow = plt.imshow(im)
