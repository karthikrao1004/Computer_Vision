import cv2

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grad_x = cv2.Sobel(gray_image, cv2.CV_8U, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray_image, cv2.CV_8U, 0, 1, ksize=3)

grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edge Detection', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()