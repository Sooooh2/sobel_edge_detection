#importing necessary modules
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#loading the image ("file_name.png"), (png/jpg) and converting into gray scale 
img = Image.open("cat.png").convert("L")
gray = np.array(img, dtype=np.float32)

#sobel kernels for x and y directions
sobel_x = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]],dtype=np.float32)

sobel_y = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]],dtype=np.float32)

# gaussian blur kernel 
gaussian_blur = np.array([
    [1,2,1],
    [2,4,2],
    [1,2,1]], dtype=np.float32) / 9  #normalizing the kernel 

# convolving function to compute image with provided kernels
def convolve(img, kernel):
    kh,kw = kernel.shape
    pad_h = kh // 2
    pad_w = kw // 2

    padded = np.pad(img, ((pad_h,pad_h), (pad_w,pad_w)), mode = 'edge')
    output = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded[i:i+kh, j:j+kw]
            output[i,j] = np.sum(region * kernel)
    
    return output

#applaying the function to get sobel filter and gaussian blur 
blurred = convolve(gray, gaussian_blur)
edge_x = convolve(blurred, sobel_x)
edge_y = convolve(blurred, sobel_y)

#calculating edge magnitude i.e thickness 
magnitude = np.sqrt(edge_x ** 2 + edge_y ** 2)
magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)


#plotting the results
plt.figure(figsize=(12,6))

# #original 
plt.subplot(1, 3, 1)
plt.title("OG")
plt.imshow(gray, cmap ='gray')

# #blurred
plt.subplot(1, 3, 2)
plt.title("Blurred")
plt.imshow(blurred, cmap = 'gray')

#edge detected 
plt.subplot(1, 3, 3)
plt.title("Sobel Edge Detection")
plt.imshow(magnitude, cmap = 'gray')

plt.tight_layout()
plt.show()