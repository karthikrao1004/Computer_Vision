import cv2
import matplotlib.pyplot as plt

def plot_histogram(image):
    hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])

    plt.plot(hist_b, color='b')
    plt.plot(hist_g, color='g')
    plt.plot(hist_r, color='r')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.title('Histogram of Color Channels')
    plt.show()

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path)
plot_histogram(image)