import cv2
import numpy as np
import matplotlib.pyplot as plt

#                                   0
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
# plt.show()
# save image 
cv2.imwrite('watchgray.png',img)