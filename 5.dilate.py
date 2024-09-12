import cv2
path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny, iterations = 10)
imgEroded = cv2.erode(imgDilation,iterations=2)
cv2.imshow("Img Erosion",imgEroded)
cv2.waitKey(0)
