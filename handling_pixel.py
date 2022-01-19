import cv2

# print(cv2.__version__)
# image = cv2.imread('srk.jpg', 1)
image1 = cv2.imread('srk.jpg', 0)
# image2 = cv2.imread('srk.jpg', -1)

print(image1.shape)
print(image1)
# cv2.imshow('color image', image)
cv2.imshow('grayscale image', image1)
# cv2.imshow('unchanged image', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('computer image', image)

# cv2.imwrite('color image', image)
# cv2.imwrite('grayscale image', image1)
# cv2.imwrite('unchanged image', image2)