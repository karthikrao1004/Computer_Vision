import cv2

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path)

larger_image = cv2.resize(image, (800, 600))
smaller_image = cv2.resize(image, (300, 200))

cv2.imshow('Original Image', image)
cv2.imshow('Larger Image', larger_image)
cv2.imshow('Smaller Image', smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()