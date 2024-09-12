import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg")  # 0 means grayscale

# Define the structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Perform the closing operation
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Show results
cv2.imshow('Original Image', image)
cv2.imshow('Closed Image', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
