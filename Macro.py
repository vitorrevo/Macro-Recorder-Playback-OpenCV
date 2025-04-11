import cv2

cap = cv2.VideoCapture('path_to_your_video_file')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    _, th1 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(th1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if(area > 200):
            x,y,w,h = cv2.boundingRect(contour)
            
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
