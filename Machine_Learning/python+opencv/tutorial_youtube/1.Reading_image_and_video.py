import cv2

# 1) Reading image
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cat.jpg'
image = cv2.imread(path)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2) Reading video
# use real time camera
capture1 = cv2.VideoCapture(0) # number in function mean you can select camera you want to ues 1, 2, 3 etc

# read video from directory file
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Videos\dog.mp4'
capture2 = cv2.VideoCapture(path)

# read video frame by frame
while True:
    isTrue, frame1 = capture1.read()
    
    cv2.imshow("video1", frame1)
    
    # stop video
    if cv2.waitKey(20) & 0xff==ord('d'):
        break
    
while True:
    isTrue, frame2 = capture2.read()
    
    cv2.imshow("video2", frame2)
    
    # stop video
    if cv2.waitKey(20) & 0xff==ord('d'):
        break
    
# control how to manage resource in computer
capture1.release()
capture2.release()
cv2.destroyAllWindows()