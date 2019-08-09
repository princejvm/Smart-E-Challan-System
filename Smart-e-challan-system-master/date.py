import numpy as np
import cv2
import datetime
# Create a black image
cam = cv2.VideoCapture('taffic.mp4')
dekhneWaala = 'taffic.mp4'
if (not cam.isOpened()):
    cam.open(dekhneWaala)
if (cam.isOpened()):
    while(1):
        ret, img = cam.read()
        #print (img.shape)
        #img = cv2.resize(img, (600,600), interpolation = cv2.INTER_AREA)
        #img = np.zeros((512,512,3), np.uint8)

        # Write some Text

        now = datetime.datetime.now()
        #print("Current date and time : ")
        tarikhSamay = now.strftime("%Y-%m-%d %H:%M:%S")
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        uparMein = (10,50)
        fontScale              = 1
        fontColor              = (255,20,25)
        lineType               = 2

        cv2.putText(img,tarikhSamay,
            uparMein,
            font,
            fontScale,
            fontColor,
            lineType)
        cv2.imshow('dikhao',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
else:
    print ("wat lagi")
cam.release()
cv2.destroyAllWindows()