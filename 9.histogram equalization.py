import cv2
import matplotlib.pyplot as plt
image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
equalized = cv2.equalizeHist(gray)
plt.subplot(1, 2, 1), plt.imshow(gray, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(equalized, cmap='gray'), plt.title('Equalized')
plt.show()
