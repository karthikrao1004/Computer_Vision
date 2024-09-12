import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_color_histogram(image_path):

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found or unable to load.")
        return
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    colors = ('r', 'g', 'b')
    plt.figure(figsize=(8, 6))
    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image_rgb[:, :, i]], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color)
    
    plt.title('Color Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend(colors)
    plt.show()


plot_color_histogram(r"C:\Users\akhil\OneDrive\Desktop\bike.jpeg")
