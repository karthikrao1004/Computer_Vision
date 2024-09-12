import cv2
import numpy as np

image = cv2.imread(r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg") 
output_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)


edges = cv2.Canny(gray, 50, 150, apertureSize=3)


lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)


if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)


circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50, param1=100, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(output_image, (x, y), r, (255, 0, 0), 3)

contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(output_image, contours, -1, (0, 0, 255), 2)


cv2.imshow('Original Image', image)
cv2.imshow('Detected Lines, Circles, and Curves', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
