import cv2

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path)

kernel = cv2.getStructElement(cv2.MORPH_RECT, (5, 5))

eroded_image = cv2.erode(image, kernel, iterations=1)
dilated_image = cv2.dilate(eroded_image, kernel, iterations=1)

top_hat_image