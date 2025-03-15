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
resize = cv2.resize(image, dsize=(50,1000), interpolation=cv2.INTER_LINEAR)
# at cv2. (command)
#cv2.INTER_NEAREST => bad quality good for sharp image fast process
#cv2.INTER_LINEAR => smooth image but have some blur
#cv2.INTER_CUBIC => smoother image more than "linear" good quality but slower
#cv2.INTER_LANCZOS4 => sharpest and most detail image slowest method 
#cv2.INTER_AREA => use for shrinking image good for downscale image

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()