import cv2 as cv

#img = cv.imread("download.png", 1 )
#cv.imshow("carrot", img)

img = cv.imread("download.png")

resized_image = cv.resize(img, (800, 600))
cv.imshow ("resize", resized_image)

cv.waitKey(0)

image = cv.imread("copy.png")

image_resized = cv.resize(image, (349, 145))
cv.imshow("resize", image_resized)

cv.waitKey(0)