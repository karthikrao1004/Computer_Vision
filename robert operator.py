import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg", cv2.IMREAD_GRAYSCALE)

# Apply Roberts operator for edge detection
kernelx = np.array([[-1, 0], [0, 1]])
kernely = np.array([[0, -1], [1, 0]])
img_rx = cv2.filter2D(img, cv2.CV_8U, kernelx)
img_ry = cv2.filter2D(img, cv2.CV_8U, kernely)

# Combine the gradient images in x and y directions
grad = cv2.addWeighted(img_rx, 0.5, img_ry, 0.5, 0)

# Display the original image and the edge detected image
cv2.imshow('Original', img)
cv2.imshow('Edges', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()
