import cv2
import numpy as np

blank = np.zeros(shape=[500,500], dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), pt1=(30,30), pt2=(400,400), color=255,thickness=-1)
cv2.imshow("rectangle", rectangle)

circle = cv2.circle(blank.copy(), center=(blank.shape[0]//2, blank.shape[1]//2), radius=100, color=255, thickness=-1)
# thickness value = -1 (fill shape)
cv2.imshow("circle", circle)

# 1) Bitwise AND
bitwise_and = cv2.bitwise_and(src1=rectangle, src2=circle)
cv2.imshow("bitwise_and", bitwise_and)

# 2) Bitwise OR
bitwise_or = cv2.bitwise_or(src1=rectangle, src2=circle)
cv2.imshow("bitwise_or", bitwise_or)

# 3) Bitwise XOR => find not intersection
bitwise_XOR = cv2.bitwise_xor(src1=rectangle, src2=circle)
cv2.imshow("bitwise_XOR", bitwise_XOR)

# 4) Bitwise NOT => output all anything that source not have
bitwise_NOT = cv2.bitwise_not(src=rectangle)
cv2.imshow("bitwise_NOT", bitwise_NOT)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()