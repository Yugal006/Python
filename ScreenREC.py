import cv2 #OpenCV
import pyautogui as pgi
import numpy
cc = cv2.VideoWriter_fourcc(*"XVID")
screen  = pgi.size()
output = cv2.VideoWriter("C:\\Users\\Admin\\Desktop\\Recorded.avi",cc,20.0,screen)
cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270)


while True:
    img = pgi.screenshot() #capturing screenshot
    frames = numpy.array(img) #converting the image into numpy array representation 
    frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB) #converting the BGR image into RGB image
    output.write(frames) #writing the RBG image to file
    cv2.imshow('Recording', frames) #display screen/frame being recorded
    if cv2.waitKey(1) == ord('q'): #Wait for the user to press 'q' key to stop the recording
        break

output.release() #closing the video file
cv2.destroyAllWindows() #destroying the recording window
