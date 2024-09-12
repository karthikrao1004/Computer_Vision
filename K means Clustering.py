import cv2
import numpy as np

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path)

# reshape image into feature vector
rows, cols, _ = image.shape
image_reshape = image.reshape((-1, 3))

# apply K-Means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness, labels, centers = cv2.kmeans(image_reshape.astype(np.float32), 5, None, criteria, 10, flags)

# map labels to colors
segmented_image = np.zeros((rows, cols, 3), dtype=np.uint8)
for i in range(5):  # Number of clusters
    segmented_image[labels.reshape(rows, cols) == i] = np.uint8(centers[i])

# visualize the clusters
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
