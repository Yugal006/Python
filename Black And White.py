import cv2
import os
ask = input("enter the image location + image name with extention:\n")
location = r'C:\Users\Admin\Desktop'
image = cv2.imread(ask)
file_name = "your_image.png"
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray)
cv2.imshow('Original Image', image)
cv2.imwrite(os.path.join(location , file_name), gray)
cv2.waitKey(0)
