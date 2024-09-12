import cv2
import numpy as np


img = cv2.imread(r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg", cv2.IMREAD_GRAYSCALE)


grad_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
grad_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

cv2.imshow('Original', img)
cv2.imshow('Edges', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()
