import cv2
import numpy as np

path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cat.jpg'
image = cv2.imread(path)

# 1) Translation => move image from x axis or y axis
def translate(image, x, y):
    translation = np.float32([[1,0,x], [0,1,y]])
    dimension = (image.shape[1], image.shape[0]) # height and width
    return cv2.warpAffine(image, M=translation, dsize=dimension)

# -x => left
# x => right
# y => down
# -y => up

translated = translate(image, 100, 100)
cv2.imshow("translated", translated)

# 2) Rotation => change angle image
def rotate(image, angle, rotation_point = None):
    (height, width) = image.shape[:2]
    print(height, width)
    if rotation_point == None:
        rotation_point = (width//2, height//2)
    
    rotMat = cv2.getRotationMatrix2D(center=rotation_point, angle=angle, scale=1.0)
    dimension = (width, height)
    
    return cv2.warpAffine(image, rotMat, dimension)

rotation = rotate(image, 45)
cv2.imshow("rotation", rotation)

# 3) Resize
resize = cv2.resize(image, dsize=(50,100), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("resize", resize)
# at cv2. (command) interpolation= use for set quality picture after you resize
#cv2.INTER_NEAREST => bad quality good for sharp image fast process
#cv2.INTER_LINEAR => smooth image but have some blur
#cv2.INTER_CUBIC => smoother image more than "linear" good quality but slower
#cv2.INTER_LANCZOS4 => sharpest and most detail image slowest method 
#cv2.INTER_AREA => use for shrinking image good for downscale image

# 4) Flip
flip = cv2.flip(image, flipCode=0) # 0 = y axis
cv2.imshow("flip0", flip)
flip = cv2.flip(image, flipCode=1) # 1 = x axis
cv2.imshow("flip1", flip)
flip = cv2.flip(image, flipCode=-1) # -1 = x and y axis
cv2.imshow("flip-1", flip)

# 5) Cropping
crop = image[200:400, 300:400]
cv2.imshow("crop", crop)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()