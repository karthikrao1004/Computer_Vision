import cv2

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path)

roi_x, roi_y, roi_w, roi_h = 100, 100, 200, 200
roi = image[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w]

pasted_image = image.copy()
pasted_image[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w] = roi

cv2.imshow('Original Image', image)
cv2.imshow('Pasted Image', pasted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()