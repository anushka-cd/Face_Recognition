
import cv2
from matplotlib import pyplot as plt
import numpy as np
gray = cv2.imread('dataSet/User.4.1.jpg', 0)
im = np.float32(gray) / 255.0# Calculate gradient
gx = cv2.Sobel(im, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(im, cv2.CV_32F, 0, 1, ksize=1)
mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
plt.figure(figsize=(12,8))
plt.imshow(mag)
plt.show()