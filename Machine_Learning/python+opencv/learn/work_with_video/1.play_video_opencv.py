import cv2
path_video = r"C:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_video\video.mp4"
cap = cv2.VideoCapture(path_video)
#VideoCapture(0) mean first camera or webcam
#VideoCapture(1) mean second camera or webcam
#VideoCapture(file_name) mean video file
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")

# Read until video complete
while(cap.isOpened()):
    # capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # display frame
        cv2.imshow("frame", frame)
        # press "g" to exist
        if cv2.waitKey() & 0xFF == ord('g'):
            break
        
    # break loop
    else:
        break;
    
# release video capture object
cap.release()
cv2.destroyAllWindows()