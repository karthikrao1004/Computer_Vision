import cv2

image = cv2.imread('C:\Users\akhil\OneDrive\Desktop\bike.jpeg')

x, y, w, h = 50, 50, 100, 100  # Example values

fill_color = (0, 0, 255)  # Red

image[y:y+h, x:x+w] = fill_color

cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('modified_image.jpg', image)
