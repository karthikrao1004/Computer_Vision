import cv2
import numpy as np

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

grad_x = cv2.filter2D(gray_image, cv2.CV_8U, kernel_x)
grad_y = cv2.filter2D(gray_image, cv2.CV_8U, kernel_y)

grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Prewitt Edge Detection', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()
