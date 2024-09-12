import cv2
import numpy as np

def region_growing(image, seed_point):
    rows, cols = image.shape[:2]
    x, y = seed_point
    neighbor_points = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    region = [seed_point]
    for point in region:
        for n_point in neighbor_points:
            nx, ny = n_point
            if 0 <= nx < rows and 0 <= ny < cols:
                if image[nx, ny] > 0 and (nx, ny) not in region:
                    region.append((nx, ny))
    return region

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

seed_point = (100, 100)  # adjust the seed point as needed
region = region_growing(image, seed_point)

# visualize the region
mask = np.zeros(image.shape, dtype=np.uint8)
for point in region:
    x, y = point
    mask[x, y] = 255

cv2.imshow('Region', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()