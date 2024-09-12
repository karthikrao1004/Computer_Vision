import cv2
import numpy as np

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path)

height, width, _ = image.shape
lower_half = image[height//2:, :, :]
mirrored_lower_half = cv2.flip(lower_half, 0)
upper_half = mirrored_lower_half

mirrored_image = np.concatenate((upper_half, lower_half), axis=0)

cv2.imshow('Mirrored Image', mirrored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()