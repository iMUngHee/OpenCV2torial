import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[:] = 255, 0, 0
# cv.imshow('Blue', blank)

# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# blank[:] = 0, 0, 255
# cv.imshow('Red', blank)

# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Red', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[1] // 2), (0, 255, 0),
#              thickness=-1)  # cv.FILLED == -1
# cv.imshow('Rectangle', blank)

# 3. Draw A Circle
# cv.circle(blank, (blank.shape[1] // 2,
#           blank.shape[1] // 2), 40, (0, 0, 255), thickness=cv.FILLED)

# cv.imshow('Circle', blank)

# 4. Draw A Line
# cv.line(blank, (0, 0), (blank.shape[1] // 2,
#                         blank.shape[1] // 2), (255, 255, 0), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello World!', (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blank)


cv.waitKey(0)
