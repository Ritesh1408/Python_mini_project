import cv2

source = "img.jpg"
destination = "resized_img.png"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow('img', src)

#percent by which the image is resized

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

#desize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)
cv2.imshow('resized image', output)
cv2.imwrite(destination, output)
cv2.waitKey(0)








