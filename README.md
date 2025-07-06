# 📐 Sobel Edge Detection

This project demonstrates **Sobel Convolution** — a widely used image processing technique to detect edges in images using Python.

We apply a **Gaussian blur** to smooth the image, then use **Sobel filters** to highlight areas where brightness changes sharply, revealing the edges of objects.

---

## 🔧 Technologies Used

- **NumPy** – for matrix operations
- **Pillow (PIL)** – for loading and converting images
- **Matplotlib** – for visualizing image output

---

###Why Gray Scale?
-Most edge detection techniques (like Sobel) work on intensity values, not color.
-Converting the image to grayscale simplifies the data to a single channel, making the calculations faster and more meaningful for detecting edges.
✅ Reduces complexity
✅ Focuses on brightness changes
✅ Ideal for edge detection

---

### Why Gaussian Blur 
- Images often contain noise that can lead to false edges.
- A Gaussian blur smooths out high-frequency details, making edge detection more accurate.

✅ Reduces noise
✅ Improves edge clarity
✅ Stabilizes results

--- 

### Defining Sobel Kernels 
Horizontal - x direciton
```python
[ -1  0  1 ]
[ -2  0  2 ]
[ -1  0  1 ]
```
Vertical - y direction
```python
[ -1 -2 -1 ]
[  0  0  0 ]
[  1  2  1 ]
```
- These kernels detect edges by highlighting areas of rapid change in brightness.
- They are applied separately to detect vertical and horizontal edges, and then combined.
```python
magnitude = np.sqrt(edge_x ** 2 + edge_y ** 2)
```

---

### Convolution Function Logic 
```python
kh, kw = kernel.shape
pad_h, pad_w = kh // 2, kw // 2
padded = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
output = np.zeros_like(img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        region = padded[i:i+kh, j:j+kw]
        output[i, j] = np.sum(region * kernel)
return output
```
- kh, kw get the kernel's height and width.
- Padding (pad_h, pad_w) ensures the output size matches the input.
- np.pad() adds border pixels to avoid edge errors during convolution.
- output = np.zeros_like(img) creates an empty result image
- The function - Slides the kernel across the image, multiplies overlapping values, and sums them to get the filtered output at each pixel.

---
  
| Original Image      | Grayscale                  | Edges Detected               |
| ------------------- | -------------------------- | ---------------------------- |
| ![input](./cat.png) | ![gray](./gray_output.png) | ![edges](./sobel_output.png) |
---

###🚀 How to Run
##1. Clone the repo
```
git clone https://github.com/yourusername/sobel-edge-detection.git
cd sobel-edge-detection
```
##2. Install dependencies
```
pip install numpy matplotlib pillow
```
## 3. Run the script
```
python sobel.py
```

 


