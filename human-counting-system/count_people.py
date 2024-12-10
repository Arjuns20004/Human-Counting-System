import cv2, imutils, time
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(0)
total = 0
print('Press q to quit')
while True:
    ret, frame = cap.read()
    if not ret: break
    frame = imutils.resize(frame, width=600)
    rects, weights = hog.detectMultiScale(frame, winStride=(8,8))
    for (x,y,w,h) in rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow('People', frame)
    total = len(rects)
    print('Detected:', total)
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break
cap.release(); cv2.destroyAllWindows()