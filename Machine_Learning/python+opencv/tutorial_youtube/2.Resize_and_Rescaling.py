import cv2

# create function to resize and rescale (work on all picture video and live video)
def rescaleFrame(frame, scale = 0.75):
    # in shape[] mean (0 height, 1 width, 2 value rgb , :2 height and width)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

# create function but it only work on live video
def changeResolution(width, height):
    video.set(3, width)
    video.set(4, height)

# 1) resize video
path_video = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Videos\dog.mp4'
video = cv2.VideoCapture(path_video)

while True:
    isTrue, frame = video.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv2.imshow("normal", frame)
    cv2.imshow("rescale", frame_resized)
    
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv2.destroyAllWindows()

# 2) resize photo
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cat.jpg'
image = cv2.imread(path)
cv2.imshow("image", image)
height, width = image.shape[:2]

resize_image = rescaleFrame(image)
cv2.imshow("rescale_image" , resize_image)

cv2.waitKey(0)
cv2.destroyAllWindows()