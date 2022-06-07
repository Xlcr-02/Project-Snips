import cv2

cam = cv2.VideoCapture(0)

while (True):
    '''
    ret , frame = cam.read()
    '''
    #to flip the video
    rval, frame = cam.read()
    frame = cv2.flip(frame,1)
    cv2.imshow('FRAME',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
