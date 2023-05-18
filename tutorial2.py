#OpenCv imported
import cv2 
import random


img = cv2.imread('Car.jpeg', -1)

#First Row of the pixel
# print(img[0])

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Mercedes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()