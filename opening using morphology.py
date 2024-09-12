import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/ankal/OneDrive/Desktop/naruto/butterfly.jpg")  # 0 means grayscale

# Define the structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Perform the opening operation
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Show results
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
