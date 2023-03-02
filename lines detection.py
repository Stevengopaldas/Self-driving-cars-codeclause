import cv2
import numpy as np

img = cv2.imread("lines.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(gray_img, 75, 150)

lines = cv2.HoughLinesP(canny_img, rho=1, theta=np.pi/180, threshold=30, maxLineGap=250)

for line in lines:
 x1, y1, x2, y2 = line[0]
cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow("Edges", canny_img)
cv2.imshow("Image", img)
cv2.imwrite("1.3_lines_with_gap.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()