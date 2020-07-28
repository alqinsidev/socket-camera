import cv2
import base64 
  
  
# define a video capture object 
wCap = cv2.VideoCapture(0) 
  
while(True): 
    wCap.set(cv2.CAP_PROP_FRAME_WIDTH,600)
    wCap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
    retval, image = wCap.read()
    retval, buffer = cv2.imencode('.jpg', image)
    data = base64.b64encode(buffer)
    print(data)