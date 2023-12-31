import cv2
body_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')

vid = cv2.VideoCapture('walking.avi')

while(True):
   
    ret, frame = vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    body= body_cascade.detectMultiScale(gray,1.2,3)
    for x,y,w,h in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Pedestrians", frame)
      
    if cv2.waitKey(25) == 32:
        break
  
vid.release()

cv2.destroyAllWindows()



