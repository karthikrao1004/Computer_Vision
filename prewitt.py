import cv2
import numpy as np

img = cv2.imread(r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg", cv2.IMREAD_GRAYSCALE)

kernelx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernely = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
img_px = cv2.filter2D(img, cv2.CV_8U, kernelx)
img_py = cv2.filter2D(img, cv2.CV_8U, kernely)

grad = cv2.addWeighted(img_px, 0.5, img_py, 0.5, 0)

cv2.imshow('Original', img)
cv2.imshow('Edges', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()
