#OpenCv imported
import cv2 

#importing the image
img = cv2.imread('Car.jpeg', 1)
#resizing the image
img = cv2.resize(img, (400,400))

#rotating the image
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Saving the image in the new folder
# cv2.imwrite('new_img.jpeg', img)

#displaying the image
cv2.imshow('Mercedes', img)
cv2.waitKey(0) #wait for the user to press any key 
cv2.destroyAllWindows() #closes the image window