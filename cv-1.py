import cv2

image_path = r"C:\Users\karth\OneDrive\Desktop\CV\A.jpeg"

print("Image Path:", image_path)

image = cv2.imread(image_path)

if image is not None:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load image. Please check the file path.")
